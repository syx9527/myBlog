// 触发点击事件，js渲染后点击失效，已经解决
$(document).on("click", "#dig .dignum", function () {

    var is_up = $(this).hasClass("ion-heart")

    $obj = $(this)

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

                var val = parseInt($obj.text());

                $obj.text(val + 1)

            } else {
                if (data.msg) {
                    $("#dig_tips p").html(data.msg).css({"opacity": "1",})
                } else {
                    if (data.handed) {
                        $("#dig_tips p").html("您已经点赞过").css({"opacity": "1",})

                    } else {
                        $("#dig_tips p").html("您已经点踩过").css({"opacity": "1",})

                    }
                    setTimeout(function () {
                        $("#dig_tips p").html('这里是操作信息').css({"opacity": '0',})
                    }, 2000)
                }
                setTimeout(function () {
                    $("#dig_tips p").html('这里是操作信息').css({"opacity": '0',})
                }, 10000)


            }

        }
    })
});