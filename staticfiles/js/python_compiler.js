// static/js/python_compiler.js

let editor = null;
let waitingForInput = false;
let pendingInputResolve = null;

function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined) {
    throw "File not found: '" + x + "'";
  }
  return Sk.builtinFiles["files"][x];
}

function outf(text) {
  const con = document.getElementById("pyConsole");
  con.value += text;
  con.scrollTop = con.scrollHeight;
}

function clearPythonOutput() {
  const con = document.getElementById("pyConsole");
  con.value = "";
  waitingForInput = false;
  pendingInputResolve = null;
}

function runPythonCode() {
  clearPythonOutput();

  const con = document.getElementById("pyConsole");
  const code = editor ? editor.getValue() : document.getElementById("pyCode").value;

  Sk.configure({
    output: outf,
    read: builtinRead,
    // execLimit қоймағанбыз → лимит жоқ
    inputfun: function (promptText) {
      // Skulpt объектісін кәдімгі JS-жолға аударамыз
      let promptStr = "";
      if (typeof promptText === "string") {
        promptStr = promptText;
      } else if (window.Sk && Sk.ffi && typeof Sk.ffi.remapToJs === "function") {
        promptStr = Sk.ffi.remapToJs(promptText) || "";
      }

      if (promptStr) {
        con.value += promptStr + " ";
        con.scrollTop = con.scrollHeight;
      }

      con.focus();
      const len = con.value.length;
      con.setSelectionRange(len, len);

      return Sk.misceval.promiseToSuspension(
        new Promise(function (resolve) {
          waitingForInput = true;
          pendingInputResolve = resolve;
        })
      );
    },
    inputfunTakesPrompt: true
  });

  const promise = Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody("<stdin>", false, code, true);
  });

  promise.then(
    function () {
      // success
    },
    function (err) {
      con.value += "\n[Қате] " + err.toString();
      con.scrollTop = con.scrollHeight;
      waitingForInput = false;
      pendingInputResolve = null;
      console.error(err);
    }
  );
}

// DOM дайын болғанда – CodeMirror және Enter listener
document.addEventListener("DOMContentLoaded", function () {
  const codeTextarea = document.getElementById("pyCode");
  const consoleEl = document.getElementById("pyConsole");

  // CodeMirror-ды қосу
  editor = CodeMirror.fromTextArea(codeTextarea, {
    mode: "python",
    theme: "material",
    lineNumbers: true,
    indentUnit: 4,
    tabSize: 4,
    autofocus: true,
  });

  // Редакторды контейнерге орау – стиль үшін
  const cmWrapper = editor.getWrapperElement();
  const parent = codeTextarea.parentElement;
  parent.classList.add("code-editor");
  parent.insertBefore(cmWrapper, codeTextarea);
  codeTextarea.style.display = "none";

  // Консольде Enter басылса – input() үшін мәнді жібереміз
  consoleEl.addEventListener("keydown", function (e) {
    if (waitingForInput && e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      const text = consoleEl.value;
      const lines = text.split(/\r?\n/);
      const lastLine = lines[lines.length - 1];

      const value = lastLine.trim();
      consoleEl.value += "\n";
      consoleEl.scrollTop = consoleEl.scrollHeight;

      if (pendingInputResolve) {
        const resolve = pendingInputResolve;
        pendingInputResolve = null;
        waitingForInput = false;
        resolve(value);
      }
    }
  });
});
