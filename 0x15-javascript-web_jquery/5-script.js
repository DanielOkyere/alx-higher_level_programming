/**
 * Adds a list of element to the list when user
 * clicks on tag
 */
$('#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
});