var app = angular.module('gnstats', []);

function alertError(response) {
    if (response.data) {
        if (response.data.error_message)
            alert(response.data.error_message);
        else
            alert(response.data);
    }
}