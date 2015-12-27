var app = angular.module('gnstats', []);

function alertError(response) {
    alert(response.data.message)
}