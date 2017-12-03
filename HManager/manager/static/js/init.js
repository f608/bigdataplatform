function addDrInput(){
    /*var html="<div class='row' style='margin-top:10px'>" +
        "\n\t<div class='col-md-5'>" +
        "\n\t\t<select class='form-control selectpicker' data-live-search='true' title='Select Dr...'  name='record_name_dr[]'> <option value='固定资产 - 办公设备 - 工作台'>固定资产 - 办公设备 - 工作台</option> <option value='固定资产 - 房屋建筑物 - 亦庄厂房'>固定资产 - 房屋建筑物 - 亦庄厂房</option> <option value='存货 - 艺术品 - 油画'>存货 - 艺术品 - 油画</option></select>" +
        "\n\t</div>" +
        "\n\t<div class='col-md-7'>" +
        "\n\t\t<div class='input-group input-icon'>" +
        "\n\t\t\t<i class='fa fa-rmb'></i> " +
        "\n\t\t\t<input type='text' class='form-control input-dr' name='record_dr[]' required='required'>" +
        "\n\t\t\t<span class='input-group-addon' onclick='addDrInput()' style='cursor: pointer' ><span class='glyphicon glyphicon-plus'></span></span> " +
        "\n\t\t\t<span class='input-group-addon dr_minus' style='cursor: pointer;' ><span class='glyphicon glyphicon-minus'></span></span>" +
        "\n\t\t</div>" +
        "\n\t</div>" +
        "\n</div>";
    $("#dr_panel").append(html);*/

    var dr_node=document.getElementById('dr_node');
    dNode=dr_node.cloneNode(true);

    var dr_panel=document.getElementById('dr_panel');
    dr_panel.appendChild(dNode);


}

$(document).on("click",".dr_minus",function(){
    if($(this).parent().parent().parent().siblings().length>1){
        $(this).parent().parent().parent().remove();
        var sum = 0;
        $("input.input-dr").each(function () {
            sum += Number($(this).val());
        });
        $("#input-dr-sum").text(sum);
        if($("#input-dr-sum").text()!=$("#input-cr-sum").text())
            $("#input-submit").attr("disabled","disabled");
        else
            $("#input-submit").removeAttr("disabled");
    }
});

function addCrInput(){
    /*var html="<div class='row' style='margin-top:10px'>" +
        "\n\t<div class='col-md-5'>" +
        "\n\t\t<select class='form-control selectpicker' data-live-search='true' title='Select Dr...'  name='record_name_cr[]'><option value='item1'>cr1</option> <option value='item2'>cr2</option> <option value='item3'>cr3</option></select>" +
        "\n\t</div>" +
        "\n\t<div class='col-md-7'>" +
        "\n\t\t<div class='input-group input-icon'>" +
        "\n\t\t\t<i class='fa fa-rmb'></i> " +
        "\n\t\t\t<input type='text' class='form-control input-cr' name='record_cr[]' required='required'>" +
        "\n\t\t\t<span class='input-group-addon' onclick='addCrInput()' style='cursor: pointer' ><span class='glyphicon glyphicon-plus'></span></span> " +
        "\n\t\t\t<span class='input-group-addon cr_minus' style='cursor: pointer;' ><span class='glyphicon glyphicon-minus'></span></span>" +
        "\n\t\t</div>" +
        "\n\t</div>" +
        "\n</div>";

        //$("#cr_panel").append(html);*/

    var cr_node=document.getElementById('cr_node');
    cNode=cr_node.cloneNode(true);

    var cr_panel=document.getElementById('cr_panel');
    cr_panel.appendChild(cNode);
    //$(".selectpicker").selectpicker();
}

$(document).on("click",".cr_minus",function(){
    if($(this).parent().parent().parent().siblings().length>1){
        $(this).parent().parent().parent().remove();

        var sum = 0;
        $("input.input-cr").each(function () {
            sum += Number($(this).val());
        });
        $("#input-cr-sum").text(sum);
        if($("#input-dr-sum").text()!=$("#input-cr-sum").text())
            $("#input-submit").attr("disabled","disabled");
        else
            $("#input-submit").removeAttr("disabled");
    }
});

/**
 * 统计借记、贷记和
 */
$(document).on('input propertychange',"input.input-dr", function() {
        var sum = 0;
        $("input.input-dr").each(function () {
            sum += Number($(this).val());
        });
        $("#input-dr-sum").text(sum);
    if($("#input-dr-sum").text()!=$("#input-cr-sum").text())
        $("#input-submit").attr("disabled","disabled");
    else
        $("#input-submit").removeAttr("disabled");
});

$(document).on('input propertychange',"input.input-cr",function(){
        var sum = 0;
        $("input.input-cr").each(function () {
            sum += Number($(this).val());
        });
        $("#input-cr-sum").text(sum);
    if($("#input-dr-sum").text()!=$("#input-cr-sum").text())
        $("#input-submit").attr("disabled","disabled");
    else
        $("#input-submit").removeAttr("disabled");
});

/**
 * 日期和时间选择器的初始化
 */
$(function () {
    $(".datepicker").datepicker({
        //language: "zh-CN",
        autoclose: true,//选中之后自动隐藏日期选择框
        clearBtn: true,//清除按钮
        //todayBtn: true,//今日按钮
        format: "yyyy-mm-dd"
    });
});

$(function () {
    $(".bootstrap-timepicker").timepicker({
        minuteStep: 1,
        secondStep: 1,
        showInputs: false,
        showSeconds: true,
        showMeridian: false,
        disableMousewheel:false
    });
});



