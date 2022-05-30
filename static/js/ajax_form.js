$(document).ready(function(){
            /*ПРОВЕРЯЕМ НАЖАТА ЛИ КНОПКА ОТПРАВКИ*/
            $('#btn_submit').click(function(){
                // собираем данные с формы
                var name    = $('#name').val();
                var email   = $('#email').val();
                var phone = $('#phone').val();
                // отправляем данные
                $.ajax({
                    url: "feedback_view", // куда отправляем
                    type: "post", // метод передачи
                    data: { // что отправляем
                        "name":    user_name,
                        "email":   user_email,
                        "phone":   user_phone,
                        "text_comment": text_comment
                    },
                    error:function(){$("#erconts").html("Произошла ошибка!");},
                    /* если произойдет ошибка в элементе с id erconts выведится сообщение*/
                    beforeSend: function() {
                        $("#erconts").html("Отправляем данные...");
                    },
                    success: function(result){
                        /* В случае удачной обработки и отправки выполнится следующий код*/
                        $('#erconts').html(result);
                        console.log("ntcn");
                    }
                });
            });
        });