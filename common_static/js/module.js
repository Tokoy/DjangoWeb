var app = angular.module('myApp', ['ngRoute','ui.bootstrap','ngAnimate','ngTouch','djng.forms']);

app.factory('MyModel', ['$resource', function($resource) {
    return $resource('/crud/mymodel/', {'pk': '@pk'}, {
    });
}]);