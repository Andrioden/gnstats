function StatsDialogController($rootScope, $scope, $mdDialog, $http) {

    // *************** PUBLIC VARIABLES ***************

    $scope.loadingData = false;
    $scope.stats = undefined;
    $scope.statsBehaviorOrderByField = 'sum_weighed';
    $scope.statsBehaviorReverseSort = true;


    // *************** CONSTRUCTOR ***************

    $scope.loadingData = true;
    $http.get('/api/actions/stats/').
        then(function (response) {
            $scope.loadingData = false;
            console.log(response);
            $scope.stats = response.data;
        }, function (response) {
            $scope.loadingData = false;
            alertError(response);
        });


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.backgroundStyle = function (performance) {
        if (performance) {
            let performancePercent = (performance.hosted + performance.best - performance.worst) / (performance.hosted * 2);
            return {
                "background-color": $scope.getColorForPercentage(performancePercent),
            }
        }
    }

    let percentColors = [
        { pct: 0.0, color: { r: 0xff, g: 0x00, b: 0 } },
        { pct: 0.5, color: { r: 0xff, g: 0xff, b: 0 } },
        { pct: 1.0, color: { r: 0x00, g: 0xff, b: 0 } }];

    // https://stackoverflow.com/a/7128796/686131
    $scope.getColorForPercentage = function (pct) {
        let index = null;
        for (let i = 1; i < percentColors.length - 1; i++) {
            if (pct < percentColors[i].pct) {
                index = i;
                break;
            }
        }
        let lower = percentColors[index - 1];
        let upper = percentColors[index];
        let range = upper.pct - lower.pct;
        let rangePct = (pct - lower.pct) / range;
        let pctLower = 1 - rangePct;
        let pctUpper = rangePct;
        let color = {
            r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
            g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
            b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
        };
        return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
        // or output as hex if preferred
    }  

    // *************** PRIVATE METHODS ***************



    console.log("StatsDialogController loaded");
}