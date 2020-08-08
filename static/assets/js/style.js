// Adjust height of textareas in edit recipe form
// https://stackoverflow.com/questions/24994395/change-the-height-and-width-of-text-area
$(document).ready(function () {
  textAreaAdjust(document.getElementById("ingredients"));
  textAreaAdjust(document.getElementById("summary"));
  textAreaAdjust(document.getElementById("steps"));
});

function textAreaAdjust(o) {
  o.style.height = o.scrollHeight + "px";
}
