// 触发点击事件，js渲染后点击失效，已经解决
$(document).on("click", "#dig .dignum", function () {

    var is_up = $(this).hasClass("ion-heart")


    // var id = this.id;
    // var name = this.getAttribute("name");
    // console.log(id, name)
    $.ajax({
        url: "/dig/",
        type: "post",


        data: {
            is_up: is_up,
            article_id: article_id,

            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),

        },

        success: function (data) {


            if (data.state) {
                console.log(data);
            } else {

                if (data.handled) {


                } else {


                }

            }
            console.log("error");


        }
    })
})
;