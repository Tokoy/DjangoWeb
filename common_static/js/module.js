var app = angular.module('myApp', ['ngRoute','ui.bootstrap','ngAnimate','ngTouch','djng.forms','infinite-scroll']);

app.factory('MyModel', ['$resource', function($resource) {
    return $resource('/crud/mymodel/', {'pk': '@pk'}, {
    });
}]);

// app.factory('Reddit', function($http) {
//   var Reddit = function() {
//     this.items = [];
//     this.busy = false;
//     this.after = '';
//   };
//
//   Reddit.prototype.nextPage = function() {
//     if (this.busy) return;
//     this.busy = true;
//
//     $http.get("/context/").success(function(data){
//       this.items = data;
//       this.after = "t3_" + this.items[this.items.length - 1].id;
//       this.busy = false;
// 	}.bind(this));
//   };
//   return Reddit;
// });
app.factory('Reddit', function($http) {
  var Reddit = function() {
    this.items = [];
    this.busy = false;
    this.after = '';
  };

  Reddit.prototype.nextPage = function() {
    if (this.busy) return;
    this.busy = true;

    var url = "https://api.reddit.com/hot?after=" + this.after + "&jsonp=JSON_CALLBACK";
    $http.jsonp(url).success(function(data) {
      var items = data.data.children;
      for (var i = 0; i < items.length; i++) {
        this.items.push(items[i].data);
      }
      this.after = "t3_" + this.items[this.items.length - 1].id;
      this.busy = false;
    }.bind(this));
  };

  return Reddit;
});