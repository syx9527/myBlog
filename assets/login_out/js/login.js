$(".login_btn").click(function () {
    console.log(555)
    $.ajax({
        url: "/login/",
        type: "post",
        data: {
            user: $("#login_user").val(),
            pwd: $("#login_pwd").val(),

            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),

        },
        success: function (data) {

            if (data.user) {
                location.href = "/"

            } else {
                // 显示提示信息
                $(".social-text").text(data.msg).css({
                    "opacity": "1",
                    "color": "red",
                })
                setTimeout(function () {
                    $(".social-text").text('这里是登录失败消息').css({"opacity": '0',})
                }, 2000)
            }
        }
    })
})

// 注册
$(".up_btn").click(function () {

    $.ajax({
        url: "/register/",
        type: "post",
        data: {
            user: $("#up_user").val(),

            pwd: $("#up_pwd").val(),
            re_pwd: $("#up_re_pwd").val(),

            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),

        },
        success: function (data) {

            if (data.user) {

                container.classList.remove("sign-up-mode");


            } else {
                // 显示提示信息
                $(".social-text").text(data.msg).css({
                    "opacity": "1",
                    "color": "red",
                })
                setTimeout(function () {
                    $(".social-text").text('这里是注册失败的消息').css({"opacity": '0',})
                }, 2000)
            }
        }
    })
})



