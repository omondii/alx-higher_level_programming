$(document).ready(function(){
    $('#add_item').click(function(){
        // Create the new element
        const newItem = $('<li>Item</li>');
        // Append the new element to UL.my_list
        $('ul.my_list').append(newItem);
    });
});