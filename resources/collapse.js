
function collapse(button) {
	var header_cell = button.parentNode
	var from_to = calculate_indexes(header_cell)
	var header_text = header_cell.childNodes[0].nodeValue

	header_cell.style.display = 'none'

	var hidden = []
	hidden.push(header_cell)

	var row = header_cell.parentNode
	var all_rows = row.parentNode.childNodes

	for (ri=row.rowIndex + 1; ri < all_rows.length; ri++) {
		var cells = all_rows[ri].childNodes

		for (ci=from_to[0]; ci <= from_to[1]; ci++){
			var cell = cells[ci]
			cell.style.display = 'none'
			hidden.push(cell)
		}
	}
	insert_reset_button(row.childNodes[0], 'reset', header_text, hidden)
}


function calculate_indexes(header_cell){
	var index = header_cell.cellIndex
	var colspan = header_cell.getAttribute('colspan')

	var to = index * colspan
	var from = to - (colspan -1)
	return [from, to]
}


function insert_reset_button(parent, klass, header_text, hidden_list) {
	var button = document.createElement('button')
	var text = document.createTextNode('Reset' + ' ' + header_text)
	
	button.to_reset = hidden_list
	button.setAttribute('onclick', 'revert(this)')
	button.setAttribute('class', klass)
	
	button.append(text)
	parent.appendChild(button)
}


function revert(button) {
	for (i=0; i < button.to_reset.length; i++) {
		button.to_reset[i].style.display = 'table-cell'
	}
	button.parentNode.removeChild(button)
}
