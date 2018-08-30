var hidden = []
var is_hidden = false


function collapse(button) {

	var header_cell = button.parentNode
	
	header_cell.style.display = 'none'
	hidden.push(header_cell)

	var header_text = header_cell.childNodes[0].nodeValue
	var row = header_cell.parentNode
	
	var first_cell = row.childNodes[0]

	var table_body = row.parentNode
	var body = table_body.parentNode.parentNode

	var no_of_cols = header_cell.getAttribute('colspan')
	console.log(no_of_cols)

	var all_rows = table_body.childNodes

	for (row_index=0; row_index < all_rows.length; row_index++) {
		var cells = all_rows[row_index].childNodes

		for (cell_index=0; cell_index < cells.length; cell_index++) {
			var current_cell = cells[cell_index]
			if (current_cell.hasAttribute('id')){
				var cell_id = current_cell.getAttribute('id')

				if (cell_id.includes(header_text)){
					current_cell.style.display = 'none'
					hidden.push(current_cell)
				}
			}
		}
	}

	if (is_hidden == false) {
		var revert_button = document.createElement('button')
		revert_button.setAttribute('onclick', 'revert(this)')
		revert_button.setAttribute('class', 'reset')
		var text = document.createTextNode('Reset')
		revert_button.append(text)
		body.prepend(revert_button)
		is_hidden = true
	}
}


function revert(button) {
	for (hidden_index=0; hidden_index < hidden.length; hidden_index++) {
		hidden[hidden_index].style.display = 'table-cell'
	}
	button.parentNode.removeChild(button)
	hidden = []
	is_hidden = false
}
