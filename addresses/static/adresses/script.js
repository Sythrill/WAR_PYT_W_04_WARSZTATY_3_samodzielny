function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+)');
        var replacement = prefix + '-' + ndx;
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
        if (el.id) el.id = el.id.replace(id_regex, replacement);
        if (el.name) el.name = el.name.replace(id_regex, replacement);
    }

function cloneMForm(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find('input').each(function () {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + prefix ).val(total);
    $(selector).after(newElement);
    var conditionRow = $('.m_form-row:not(:last)');
    conditionRow.find('.btn.add-m_form-row')
        .removeClass('btn-success').addClass('btn-danger')
        .removeClass('add-m_form-row').addClass('remove-m_form-row')
        .html('-');
    return false;
}

function clonePForm(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find('input').each(function () {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + prefix ).val(total);
    $(selector).after(newElement);
    var conditionRow = $('.p_form-row:not(:last)');
    conditionRow.find('.btn.add-p_form-row')
        .removeClass('btn-success').addClass('btn-danger')
        .removeClass('add-p_form-row').addClass('remove-p_form-row')
        .html('-');
    return false;
}

function deleteMForm(prefix, btn) {{
    btn.closest('.m_form-row').remove();
    var forms = $('.m_form-row');
    console.log("jestem");
    $('#id_' + prefix).val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).find(':input').each(function () {
            updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}


function deletePForm(prefix, btn) {{
    btn.closest('.p_form-row').remove();
    var forms = $('.m_form-row');
    $('#id_' + prefix).val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).find(':input').each(function () {
            updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}

$(document).on('click', '.add-m_form-row', function (e) {
    e.preventDefault();
    cloneMForm('.m_form-row:last', 'form');
    return false;
});

$(document).on('click', '.remove-m_form-row', function (e) {
    e.preventDefault();
    deleteMForm('form', $(this));

    return false;
});

$(document).on('click', '.add-p_form-row', function (e) {
    e.preventDefault();
    clonePForm('.p_form-row:last', 'form');
    return false;
});

$(document).on('click', 'remove-p_form-row', function (e) {
    e.preventDefault();
    deletePForm('form', $(this));

    return false;
});
