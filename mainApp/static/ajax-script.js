//Отправляем ajax запрос на сервер
$ajax({
type: "GET",
url: 'add_know/'
data: {
'id':$( "#add_know").val(),
},
});