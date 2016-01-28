(function () {
    'use strict';
    angular.module('statusMapService', [])
        .factory('statusMapService', statusMapService);

    function statusMapService() {
        var statusMapVals = {};
        statusMapVals['Received'] = 'label-warning';
        statusMapVals['Processing'] = 'xo-label-install';
        statusMapVals['PROCESSING'] = 'xo-label-install';
        statusMapVals['Dispatching'] = 'xo-label-install';
        statusMapVals['Activating'] = 'xo-label-install';
        statusMapVals['Active'] = 'xo-label-general';
        statusMapVals['Cancelled'] = 'xo-label-closed';
        statusMapVals['Action Required'] = 'label-danger';
        statusMapVals['In Progress'] = 'label-warning';
        statusMapVals['Pending'] = 'label-warning';
        statusMapVals['Pending Disconnect'] = 'statusYellow';
        statusMapVals['Scheduled'] = 'label-warning';
        statusMapVals['Monitor'] = 'label-warning';
        statusMapVals['Open'] = 'label-warning';
        statusMapVals['Resolved'] = 'xo-label-general';
        statusMapVals['XO Repair'] = 'label-danger';
        statusMapVals['Vendor Repair'] = 'label-warning';
        statusMapVals['Customer Repair'] = 'xo-label-general';
        statusMapVals['Closed'] = 'xo-label-closed';
        statusMapVals['Archive'] = 'xo-label-closed';
        statusMapVals['Resolved for Closure'] = 'xo-label-closed';
        statusMapVals['Complete'] = 'xo-label-general';
        statusMapVals['APPROVED'] = 'xo-label-general';
        statusMapVals['SUBMITTED'] = 'label-warning';
        statusMapVals['DECLINED'] = 'label-danger';
        statusMapVals['In Service'] = 'xo-label-general';
        statusMapVals['Disconnected'] = 'label-danger';
        statusMapVals['Cleared'] = 'xo-label-general';

        var eventClassMapVals = {};
        eventClassMapVals['#c23939'] = 'label-danger';
        eventClassMapVals['#5db56b'] = 'xo-label-general';
        eventClassMapVals['#8d9399'] = 'xo-label-closed';
        eventClassMapVals['#d77e1c'] = 'statusOrange';
        eventClassMapVals['#ecc200'] = 'label-warning';

        var service = {
            statusMap: statusMapVals,
            eventClassMap: eventClassMapVals
        };

        return service;

    }

})();