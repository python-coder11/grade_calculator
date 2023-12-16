function updateTestFields() {
    var numTests = document.getElementById('num_of_tests').value;
    var container = document.getElementById('testFieldsContainer');
    var group = document.getElementById('testFieldsGroup');

    if (numTests > 0) {
        group.style.display = 'block';
        container.innerHTML = '';

        for (var i = 0; i < numTests; i++) {
            var div = document.createElement('div');
            div.className = 'col-md-4 mb-3';
            div.innerHTML = '<label for="test_' + (i+1) + '">Test ' + (i+1) + ' Grade</label>' +
                                '<input type="text" class="form-control" name="test_' + (i+1) + '" required>';
            container.appendChild(div);
        }
    } else {
        group.style.display = 'none';
    }
}

    document.getElementById('num_of_tests').addEventListener('input', updateTestFields);
    updateTestFields();
