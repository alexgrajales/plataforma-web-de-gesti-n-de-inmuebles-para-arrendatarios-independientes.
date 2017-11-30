
(function () {
    'use strict';
    angular.module('usuario.demo')
        .directive('usuarioUsuario', UsuarioDirective);

    function UsuarioDirective() {
        return {
            templateUrl: '/static/usuario/usuario.html', 
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http){        
                // console.log($scope)        
                // var url = '/apiusuario/usuario/'+$scope.usuario.id + '/';                
                //  $scope.update = function(){
                //      $http.put(url, $scope.usuario
                //      );
                //  };


                $scope.delete = function(){                    
                    $http.delete(url).then(
                        function(){
                            var usuarios = $scope.list.usuarios;
                            cards.splice(usuarios.indexOf($scope.usuario), 1);
                        }
                    );                    
                };


                $scope.modelOptions = {
                    debounce: 500
                };
            }]            
        };
    }       
})();