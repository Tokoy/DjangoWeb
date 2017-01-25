// -*- coding: utf-8 -*-
'use strict';
// configure our routes
app.config(function($routeProvider,$locationProvider,$interpolateProvider,$httpProvider) {
	$routeProvider
		// route for the home page
//		.when('/', {
//			templateUrl : 'pages/home.html',
//			controller  : ''
//		})

//		// route for the login page
//		.when('/login', {
//			templateUrl : 'pages/login.html',
//			controller  : ''
//		})
//
//		// route for the register page
//		.when('/register', {
//			templateUrl : 'pages/register.html',
//			controller  : ''
//		})
		 // use the HTML5 History API
        $locationProvider.html5Mode(false);

         $interpolateProvider.startSymbol('{$');
         $interpolateProvider.endSymbol('$}');
         $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        // 解决csrftoken跨域问题 csrfFail
         $httpProvider.defaults.xsrfCookieName = 'csrftoken';
         $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
// create the controller and inject Angular's $scope
app.controller('myCtrl',function($scope,$http) {
	$scope.visible = false;
	$scope.toggle = function(){
		$scope.visible = !$scope.visible;
	}

//	RESTful框架，数据存储在url里，只需要对url进行get就可以获取json格式的数据
	$http.get("/context/").success(function(response){
		$scope.datas = response;
		//alert(JSON.stringify($scope.datas));//这样获取到的只是整个json的内容。
		//alert(JSON.stringify($scope.datas.id));这样返回的值是undefined。
	}).error(function(){})

	  $scope.oneAtATime = true;

	  $scope.groups = [
		{
		  title: 'Dynamic Group Header - 1',
		  content: 'Dynamic Group Body - 1'
		},
		{
		  title: 'Dynamic Group Header - 2',
		  content: 'Dynamic Group Body - 2'
		}
	  ];

    $scope.signup=function(){
        var datas={'name':$scope.user.displayName,
                    'password':$scope.user.password,
                    'email':$scope.user.email
                    }
        $http({
        url:'/users/',
        method:'POST',
        data:datas,
        dataType:'json'
        }).success(function(response){

		}).error(function(response){
		alert(response)
		})
    };

	  $scope.items = ['Item 1', 'Item 2', 'Item 3'];
	  $scope.addpage = function() {
		  var Title='addtitle'
		  var Content='this is add content'
		  var Person='somebody'
		  var Time = '2017/1'
		  var newdata={Title,Content,Person,Time}
		  $scope.datas.unshift(newdata)
		  
	  };
	  $scope.addItem = function() {
		var newItemNo = $scope.items.length + 1;
		$scope.items.push('Item ' + newItemNo);
	  };

	  $scope.status = {
		isCustomHeaderOpen: false,
		isFirstOpen: true,
		isFirstDisabled: false
	  };
	});
$(function(){
        $(".register").click(function(){
            $("#registermodal").modal("toggle");
        });
		$(".login").click(function(){
            $("#loginmodal").modal("toggle");
        });
		$('.carousel').carousel({
		  interval: 8000
		})
    });

$(function() {
		$(window).scroll(function(){
			if ($(this).scrollTop() > 100) {
				$('#back-to-top').fadeIn();
			} else {
				$('#back-to-top').fadeOut();
			}
		});
		$('#back-to-top').on('click', function(e){
			e.preventDefault();
			$('html, body').animate({scrollTop : 0},1000);
			return false;
		});
	});