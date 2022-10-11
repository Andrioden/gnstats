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
    alert(`${response.status}: ${response.data.detail}`);
}