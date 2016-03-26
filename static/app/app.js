var app = angular.module('gnstats', []);

function alertError(response) {
    if (response.data) {
        if (response.data.error_message)
            alert(response.data.error_message);
        else
            alert(response.data);
    }
}

Date.prototype.yyyy_mm_dd = function() {
    var yyyy = this.getFullYear().toString();
    var mm = (this.getMonth()+1).toString(); // getMonth() is zero-based
    var dd  = this.getDate().toString();
    return yyyy + "-" + (mm[1]?mm:"0"+mm[0]) + "-" + (dd[1]?dd:"0"+dd[0]); // padding
};