let app = angular.module('gnstats', ['ngMaterial', 'ngCacheBuster']);

angular.module('gnstats')
    .config(function ($mdDateLocaleProvider) {
        $mdDateLocaleProvider.formatDate = function (date) {
            return moment(date).format('DD/MM/YYYY');
        };
        $mdDateLocaleProvider.parseDate = function (dateString) {
            let m = moment(dateString, 'DD/MM/YYYY', true);
            return m.isValid() ? m.toDate() : new Date(NaN);
        };
    })
    .config(function(httpRequestInterceptorCacheBusterProvider){
        httpRequestInterceptorCacheBusterProvider.setMatchlist([/.*.html/],true);
    });

function alertError(response) {
    if (response.error_message)
        alert(response.error_message);
    else if (response.data) {
        if (response.data.error_message)
            alert(response.data.error_message);
        else
            alert(response.data);
    }
}