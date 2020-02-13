/*
Script that adds a LI element to a list when the user clicks on the tag DIV#add_item
*/
function addItem () {
  $('.my_list').append('<li>Item</li>');
}

$('#add_item').click(function () {
  addItem();
});
