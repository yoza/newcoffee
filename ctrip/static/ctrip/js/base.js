(function($) {

    cloneRow = function(selector, type, calback) {
        /* Thank you Paolo Bergantino */
        /* Add new inline formset row */
        var newElement = $(selector).clone(true);
        var total = $('#id_' + type + '-TOTAL_FORMS').val();
        newElement.find(':input').each(function() {
            var name = $(this).attr('name')
                .replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('')
                .removeAttr('checked');
        });
        newElement.find('label').each(function() {
            var newFor = $(this).attr('for')
                .replace('-' + (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
        });
        newElement.find('.char-left').first().text('');
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);
        calback(newElement);
    };

    items_delete = function(container, ctrl, form, slug, cfmsg) {
        /*** delete items from list
        /**  September 27, 2013 Oleg Prans <oleg@prans.net>
        ***/
        $(ctrl).bind('click', function(e) {
            e.preventDefault();
            var conf = confirm(cfmsg);
            if(conf == true) {
                var url = $(e.target).attr('href').replace(/^.*#/, '');
                var data = $(form).serialize();
                if (slug) {
                    data += '&slug=' + slug;
                }
                $.ajax({
                    'url': url,
                    'type': 'POST',
                    'data': data,
                    'success': function(result){
                        if (result.success) {
                            if (result.new_url) {
                                window.location = window.location.protocol
                                    + "//" + window.location.host
                                    + result.new_url;
                            } else {
                                $(ctrl).unbind('click');
                                $(container).html(result.html);
                                item_delete(container, ctrl, form,
                                            slug, cfmsg);
                            }
                        }
                    }
                });
            }
        });
    };

})(jQuery.noConflict());
