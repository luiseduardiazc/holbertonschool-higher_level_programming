/* script that updates the text color of the HTML tag HEADER to red (#FF0000)
when the user clicks on the tag DIV#red_header */
const header = document.querySelector('#red_header');
header.onclick = function () { header.style.color = '#FF0000'; };
