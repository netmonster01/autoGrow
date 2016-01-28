var raspberrypiGrowApp = angular.module('raspberrypiGrowApp', [
  'ngRoute',
  'raspberryPiDashboardCtrls',
  'raspberryPiSettingsCtrls',
  'statusMapService'
]);

raspberrypiGrowApp.config(['$routeProvider',
  function ($routeProvider) {
      $routeProvider.
        when('/', {
            templateUrl: '/static/app/views/dashboard.html',
            controller: 'raspberryPiDashboardCtrls'
        })
          .when('/settings', {
             templateUrl: '/static/app/views/settings.html',
             controller: 'raspberryPiSettingsCtrls'
         });
       
  }]);
