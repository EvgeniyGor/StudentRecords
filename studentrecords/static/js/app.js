$(document).ready(function () {
    var getItemValues = function (item) {
        var $item = $(item);
        return [
            $item.find('span[js-key="first_name"]').attr('js-value'),
            $item.find('span[js-key="last_name"]').attr('js-value'),
            $item.find('span[js-key="patronymic"]').attr('js-value'),
            $item.find('span[js-key="study_group"]').attr('js-value'),
            $item.find('span[js-key="email"]').attr('js-value'),
            $item.find('span[js-key="github"]').attr('js-value'),
            $item.find('span[js-key="stepic"]').attr('js-value')
        ];
    };

    var getFilterValues = function () {
        var filterbox = $('#filter-box');

        return [
            filterbox.find('#first-name').val(),
            filterbox.find('#last-name').val(),
            filterbox.find('#patronymic').val(),
            filterbox.find('#group').val(),
            filterbox.find('#e-mail').val(),
            filterbox.find('#github').val(),
            filterbox.find('#stepic').val()
        ];
    };

    var filterFunction = function (container, filterValues, getItemValuesFunc) {
        $(container).each(function (index, item) {
            var itemValues = getItemValuesFunc(item);
            var valuesCount = itemValues.length;
            var shouldAppear = true;

            for (var i = 0; i < valuesCount; ++i) {
                if (filterValues[i] === '') {
                    continue;
                }
                if (filterValues[i] !== itemValues[i]) {
                    shouldAppear = false;
                    break;
                }
            }

            if (shouldAppear) {
                $(item).show();
            } else {
                $(item).hide();
            }
        });
    };

    var studentsFilter = function() {
        filterFunction('.student-block', getFilterValues(), getItemValues);
    };

    $('#apply-students-filter').on('click', studentsFilter);
});