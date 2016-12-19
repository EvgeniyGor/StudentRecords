$(document).ready(function () {
    var getItemValues = function (item) {
        var $item = $(item);
        return [
            $item.find('span[key="first_name"]').text(),
            $item.find('span[key="last_name"]').text(),
            $item.find('span[key="patronymic"]').text(),
            $item.find('span[key="study_group"]').text(),
            $item.find('span[key="email"]').text(),
            $item.find('span[key="github"]').text(),
            $item.find('span[key="stepic"]').text()
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