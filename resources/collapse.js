var hidden_dict = {}


function collapse(button) {
	var hidden = []

	var header_cell = button.parentNode

	var id = header_cell + Math.random().toString()

	var text = document.createTextNode('Reset' + ' ' + header_text)
	
	header_cell.style.display = 'none'
	hidden.push(header_cell)

	var header_text = header_cell.childNodes[0].nodeValue
	var row = header_cell.parentNode
	
	var first_cell = row.childNodes[0]

	insert_reset_button(first_cell, 'reset', id, text)

	var all_rows = row.parentNode.childNodes

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

	hidden_dict[id] = hidden
}


function insert_reset_button(parent, klass, id, text_node) {
	var button = document.createElement('button')
	button.setAttribute('onclick', 'revert(this)')
	button.setAttribute('class', klass)
	button.setAttribute('id', id)
	
	button.append(text_node)
	parent.appendChild(button)
}


function revert(button) {
	var hidden = hidden_dict[button.getAttribute('id')]
	for (hidden_index=0; hidden_index < hidden.length; hidden_index++) {
		hidden[hidden_index].style.display = 'table-cell'
	}
	button.parentNode.removeChild(button)
}
