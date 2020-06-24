$('#ul_left').click(function(){
    alert("Nota: Butoanele din partea stanga nu proceseaza imaginea acumulativ.\nFiecare proces va fi actionat pe imaginea incarcata original sau imaginea modificata folosind lista de butoane din partea dreapta, dar procesele nu vor fi salvate pentru modificari ulterioare.");
    $(this).off("click");
});
$('#ul_right').click(function(){
    alert("Nota: Butoanele din partea dreapta proceseaza imaginea acumulativ.\nFiecare proces aplicat imaginii va fi actionat si salvat.");
    $(this).off("click");
});
$('#save').click(function(){
    var a  = document.createElement('a');
    a.href = $('#display_image').attr("src")
    a.download = "processed_image.jpg";
    a.click()
});
$('#original').click(function(){
    $('#display_image').attr('src',"static/uploads/imgoriginal.png");
});
$('#rgb2gray').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/rgb_to_gray',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_gray + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#im2bw').click(function(){
    $('#im2bw_slider').toggle("slow");
    $('#outputim2bw').text($('#im2bw_value').val());
    $('#im2bw_value').on('input', function(){
        $('#outputim2bw').text($(this).val());            
    });
    $('#exec_im2bw').click(function(){
        $('#im2bw_slider').hide("slow");
        $('#loading').text("Se incarca...");
        var prag = $('#im2bw_value').val();
        $.ajax({
            type: 'POST',
            url: '/gray_to_binary',
            data: prag,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_bw + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
    });
});
$('#unif_filt').click(function(){
    $('#mask_opts_unif').toggle("slow");
    $('#exec_mask_unif').click(function(){
        $('#mask_opts_unif').hide("slow");
        if(document.getElementById('mask_3x3_unif').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
            type: 'POST',
            url: '/uniform_filter_3x3',
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_unif_3x3 + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
        }else if(document.getElementById('mask_5x5_unif').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
            type: 'POST',
            url: '/uniform_filter_5x5',
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_unif_5x5 + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
        }
    });
});
$('#gauss_filt').click(function(){
    $('#mask_opts_gauss').toggle("slow");
    $('#exec_mask_gauss').click(function(){
        $('#mask_opts_gauss').hide("slow");
        if(document.getElementById('mask_3x3_gauss').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/gauss_filter_3x3',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_gauss_3x3 + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('mask_5x5_gauss').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/gauss_filter_5x5',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_gauss_5x5 + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }
    });
});
$('#roberts').click(function(){
    $('#roberts_opt').toggle("slow");
    $('#exec_roberts').click(function(){
        $('#roberts_opt').hide("slow");
        if(document.getElementById('nord_roberts').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/roberts_filter_N',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_roberts_N + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('est_roberts').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/roberts_filter_E',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_roberts_E + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('sud_roberts').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/roberts_filter_S',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_roberts_S + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('vest_roberts').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/roberts_filter_V',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_roberts_V + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }
    });
});
$('#prewitt').click(function(){
    $('#prewitt_opt').toggle("slow");
    $('#exec_prewitt').click(function(){
        $('#prewitt_opt').hide("slow");
        if(document.getElementById('nord_prewitt').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/prewitt_filter_N',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_prewitt_N + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('est_prewitt').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/prewitt_filter_E',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_prewitt_E + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('sud_prewitt').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/prewitt_filter_S',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_prewitt_S + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('vest_prewitt').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/prewitt_filter_V',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_prewitt_V + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }
    });
});
$('#sobel').click(function(){
    $('#sobel_opt').toggle("slow");
    $('#exec_sobel').click(function(){
        $('#sobel_opt').hide("slow");
        if(document.getElementById('nord_sobel').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/sobel_filter_N',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_sobel_N + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('est_sobel').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/sobel_filter_E',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_sobel_E + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('sud_sobel').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/sobel_filter_S',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_sobel_S + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('vest_sobel').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/sobel_filter_V',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_sobel_V + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }
    });
});
$('#kirsch').click(function(){
    $('#kirsch_opt').toggle("slow");
    $('#exec_kirsch').click(function(){
        $('#kirsch_opt').hide("slow");
        if(document.getElementById('nord_kirsch').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/kirsch_filter_N',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_kirsch_N + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('est_kirsch').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/kirsch_filter_E',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_kirsch_E + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('sud_kirsch').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/kirsch_filter_S',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_kirsch_S + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }else if(document.getElementById('vest_kirsch').checked) {
            $('#loading').text("Se incarca...");
            $.ajax({
                type: 'POST',
                url: '/kirsch_filter_V',
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_kirsch_V + "?a=" + performance.now());
                    $('#loading').text("");
                },
            });
        }
    });
});
$('#min_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/min_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_min + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#max_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/max_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_max + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#median_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/median_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_median + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#medext_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/medext_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_medext + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#range_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/range_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_range + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#disprange_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/disprange_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_disprange + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#alphamed_filt').click(function(){
    $('#alphamed_slider').toggle("slow");
    $('#outputmed').text($('#alphamed_value').val());
    $('#alphamed_value').on('input', function(){
        $('#outputmed').text($(this).val());          
    });
    $('#exec_alphamed').click(function(){
        $('#alphamed_slider').hide("slow");
        $('#loading').text("Se incarca...");
        var alpha = $('#alphamed_value').val();
        $.ajax({
            type: 'POST',
            url: '/alphamed_filter',
            data: alpha,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_alphamed + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
    });
});
$('#alphacom_filt').click(function(){
    $('#alphacom_slider').toggle("slow");
    $('#outputcom').text($('#alphacom_value').val());
    $('#alphacom_value').on('input', function(){
        $('#outputcom').text($(this).val());            
    });
    $('#exec_alphacom').click(function(){
        $('#alphacom_slider').hide("slow");
        $('#loading').text("Se incarca...");
        var alpha = $('#alphacom_value').val();
        $.ajax({
            type: 'POST',
            url: '/alphacom_filter',
            data: alpha,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_alphacom + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
    });
});
$('#alphaqsr_filt').click(function(){
    $('#alphaqsr_slider').toggle("slow");
    $('#outputqsr').text($('#alphaqsr_value').val());
    $('#alphaqsr_value').on('input', function(){
        $('#outputqsr').text($(this).val());           
    });
    $('#exec_alphaqsr').click(function(){
        $('#alphaqsr_slider').hide("slow");
        $('#loading').text("Se incarca...");
        var alpha = $('#alphaqsr_value').val();
        $.ajax({
            type: 'POST',
            url: '/alphaqsr_filter',
            data: alpha,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_alphaqsr + "?a=" + performance.now());
                $('#loading').text("");
            },
        });
    });
});
$('#artm_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/artm_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_artm + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#geom_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/geom_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_geom + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#harm_filt').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/harm_filter',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_harm + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#contraharm_filt').click(function(){
    $('#alphach_slider').toggle("slow");
    $('#outputch').text($('#alphach_value').val());
    $('#alphach_value').on('input', function(){
        $('#outputch').text($(this).val());              
    });
    $('#exec_alphach').click(function(){
        $('#alphach_slider').hide("slow");
        $('#loading').text("Se incarca...");
        var alpha = $('#alphach_value').val();
        $.ajax({
            type: 'POST',
            url: '/alphach_filter',
            data: alpha,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_alphach + "?a=" + performance.now());
                $('#loading').text("");
            },
        }); 
    });
});
$('#power_filt').click(function(){
    $('#power_opts').toggle('slow');
    $('#outputpow').text($('#alphapow_value').val());
    $('#alphapow_value').on('input', function(){
        $('#outputpow').text($(this).val());              
    });
    $('#outputpow2').text($('#alphapow2_value').val());
    $('#alphapow2_value').on('input', function(){
        $('#outputpow2').text($(this).val());              
    });
    $('#alphapow').on('input',function(){
        $('#exec_alphapow').click(function(){
            $('#loading').text("Se incarca...");
            var alpha = $('#alphapow_value').val();
            $.ajax({
                type: 'POST',
                url: '/alphapow_filter',
                data: alpha,
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_alphapow + "?a=" + performance.now());
                    $('#loading').text("");
                    $('#power_opts').hide('slow');
                },
            }); 
        });
    });
    $('#alphapow2').on('input',function(){
        $('#exec_alphapow').click(function(){
            $('#loading').text("Se incarca...");
            var alpha2 = $('#alphapow2_value').val();
            $.ajax({
                type: 'POST',
                url: '/alphapow2_filter',
                data: alpha2,
                success: function(resp){
                    $('#display_image').attr('src',resp.image_url_alphapow2 + "?a=" + performance.now());
                    $('#loading').text("");
                    $('#power_opts').hide('slow');
                },
            }); 
        });
    });
});
$('#bright').click(function(){
    $('#bright_slider').toggle("slow");
    $('#outputbright').text($('#bright_value').val());
    $('#bright_value').on('input', function(){
        $('#outputbright').text($(this).val());
        var factor = $('#bright_value').val();
        $.ajax({
            type: 'POST',
            url: '/bright',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_bright + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_bright').click(function(){
        var factor = $('#bright_value').val();
        $('#bright_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_bright',
            data: factor,
        });
    });
});
$('#contrast').click(function(){
    $('#contrast_slider').toggle("slow");
    $('#outputcontrast').text($('#contrast_value').val());
    $('#contrast_value').on('input', function(){
        $('#outputcontrast').text($(this).val());
        var factor = $('#contrast_value').val();
        $.ajax({
            type: 'POST',
            url: '/contrast',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_contrast + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_contrast').click(function(){
        var factor = $('#contrast_value').val();
        $('#contrast_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_contrast',
            data: factor,
        });
    });
});
$('#sharp').click(function(){
    $('#sharp_slider').toggle("slow");
    $('#outputsharp').text($('#sharp_value').val());
    $('#sharp_value').on('input', function(){
        $('#outputsharp').text($(this).val());
        var factor = $('#sharp_value').val();
        $.ajax({
            type: 'POST',
            url: '/sharp',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_sharp + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_sharp').click(function(){
        var factor = $('#sharp_value').val();
        $('#sharp_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_sharp',
            data: factor,
        });
    });
});
$('#sat').click(function(){
    $('#sat_slider').toggle("slow");
    $('#outputsat').text($('#sat_value').val());
    $('#sat_value').on('input', function(){
        $('#outputsat').text($(this).val());
        var factor = $('#sat_value').val();
        $.ajax({
            type: 'POST',
            url: '/sat',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_sat + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_sat').click(function(){
        var factor = $('#sat_value').val();
        $('#sat_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_sat',
            data: factor,
        });
    });
});
$('#autocont').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/autocont',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_autocont + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#scalare').click(function(){
    $('#scale_slider').toggle("slow");
    $('#outputscale').text($('#scale_value').val());
    $('#scale_value').on('input', function(){
        $('#outputscale').text($(this).val());
        var factor = $('#scale_value').val();
        $.ajax({
            type: 'POST',
            url: '/scalare',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_scale + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_scale').click(function(){
        var factor = $('#scale_value').val();
        $('#scale_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_scale',
            data: factor,
        });
    });
});
$('#flip').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/flip_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_flip + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#mirror').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/mirror_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_mirror + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#invert').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/invert_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_invert + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#crop').click(function(){
    $('#crop_sliders').toggle("slow");
    $('#outputleft').text($('#left_crop_value').val());
    $('#left_crop_value').on('input', function(){
        $('#outputleft').text($(this).val());
        var left = $('#left_crop_value').val();
        var upper = $('#upper_crop_value').val();
        var right = $('#right_crop_value').val();
        var lower = $('#lower_crop_value').val();
        $.ajax({
            type: 'POST',
            url: '/cropper',
            data: {left: left, upper: upper, right: right, lower: lower},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_crop + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#outputupper').text($('#upper_crop_value').val());
    $('#upper_crop_value').on('input', function(){
        $('#outputupper').text($(this).val());
        var left = $('#left_crop_value').val();
        var upper = $('#upper_crop_value').val();
        var right = $('#right_crop_value').val();
        var lower = $('#lower_crop_value').val();
        $.ajax({
            type: 'POST',
            url: '/cropper',
            data: {left: left, upper: upper, right: right, lower: lower},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_crop + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#outputright').text($('#right_crop_value').val());
    $('#right_crop_value').on('input', function(){
        $('#outputright').text($(this).val());
        var left = $('#left_crop_value').val();
        var upper = $('#upper_crop_value').val();
        var right = $('#right_crop_value').val();
        var lower = $('#lower_crop_value').val();
        $.ajax({
            type: 'POST',
            url: '/cropper',
            data: {left: left, upper: upper, right: right, lower: lower},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_crop + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#outputlower').text($('#lower_crop_value').val());
    $('#lower_crop_value').on('input', function(){
        $('#outputlower').text($(this).val());
        var left = $('#left_crop_value').val();
        var upper = $('#upper_crop_value').val();
        var right = $('#right_crop_value').val();
        var lower = $('#lower_crop_value').val();
        $.ajax({
            type: 'POST',
            url: '/cropper',
            data: {left: left, upper: upper, right: right, lower: lower},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_crop + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_crop').click(function(){
        var left = $('#left_crop_value').val();
        var upper = $('#upper_crop_value').val();
        var right = $('#right_crop_value').val();
        var lower = $('#lower_crop_value').val();
        $('#crop_sliders').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_crop',
            data: {left: left, upper: upper, right: right, lower: lower},
        });
    });
});
$('#rotate_image').click(function(){
    $('#rotate_slider').toggle("slow");
    $('#outputrotate').text($('#rotate_value').val());
    $('#rotate_value').on('input', function(){
        $('#outputrotate').text($(this).val());
        var factor = $('#rotate_value').val();
        $.ajax({
            type: 'POST',
            url: '/rotate_image',
            data: factor,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_rotate + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_rotate').click(function(){
        var factor = $('#rotate_value').val();
        $('#rotate_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_rotate',
            data: factor,
        });
    });
});
$('#rotate_90_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/rotate_90_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_rotate_90 + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#equalizer').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/equalizer',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_equalize+ "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#blur_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/blur_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_blur + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#bblur').click(function(){
    $('#bblur_slider').toggle("slow");
    $('#outputbblur').text($('#bblur_value').val());
    $('#bblur_value').on('input', function(){
        $('#outputbblur').text($(this).val());
        var radius = $('#bblur_value').val();
        $.ajax({
            type: 'POST',
            url: '/bblur',
            data: radius,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_bblur + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_bblur').click(function(){
        var radius = $('#bblur_value').val();
        $('#bblur_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_bblur',
            data: radius,
        });
    });
});
$('#gblur').click(function(){
    $('#gblur_slider').toggle("slow");
    $('#outputgblur').text($('#gblur_value').val());
    $('#gblur_value').on('input', function(){
        $('#outputgblur').text($(this).val());
        var radius = $('#gblur_value').val();
        $.ajax({
            type: 'POST',
            url: '/gblur',
            data: radius,
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_gblur + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_gblur').click(function(){
        var radius = $('#gblur_value').val();
        $('#gblur_slider').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_gblur',
            data: radius
        });
    });
});
$('#sharpen_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/sharpen_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_sharpen + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#unsharp').click(function(){
    $('#unsharp_sliders').toggle("slow");
    $('#outputradius').text($('#radius_value').val());
    $('#radius_value').on('input', function(){
        $('#outputradius').text($(this).val());
        var radius = $('#radius_value').val();
        var strength = $('#strength_value').val();
        var threshold = $('#threshold_value').val();
        $.ajax({
            type: 'POST',
            url: '/unsharp',
            data: {radius: radius, strength: strength, threshold: threshold},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_unsharp + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#outputstrength').text($('#strength_value').val());
    $('#strength_value').on('input', function(){
        $('#outputstrength').text($(this).val());
        var radius = $('#radius_value').val();
        var strength = $('#strength_value').val();
        var threshold = $('#threshold_value').val();
        $.ajax({
            type: 'POST',
            url: '/unsharp',
            data: {radius: radius, strength: strength, threshold: threshold},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_unsharp + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#outputthreshold').text($('#threshold_value').val());
    $('#threshold_value').on('input', function(){
        $('#outputthreshold').text($(this).val());
        var radius = $('#radius_value').val();
        var strength = $('#strength_value').val();
        var threshold = $('#threshold_value').val();
        $.ajax({
            type: 'POST',
            url: '/unsharp',
            data: {radius: radius, strength: strength, threshold: threshold},
            success: function(resp){
                $('#display_image').attr('src',resp.image_url_unsharp + "?a=" + performance.now());
                $('#loading').text("");
            },
        });               
    });
    $('#exec_unsharp').click(function(){
        var radius = $('#radius_value').val();
        var strength = $('#strength_value').val();
        var threshold = $('#threshold_value').val();
        $('#unsharp_sliders').hide("slow");
        $.ajax({
            type: 'POST',
            url: '/save_unsharp',
            data: {radius: radius, strength: strength, threshold: threshold},
        });
    });
});
$('#contour_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/contour_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_contour + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#detail_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/detail_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_detail + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#edge_enhance_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/edge_enhance_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_edge_enhance+ "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#emboss_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/emboss_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_emboss + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});
$('#smooth_image').click(function(){
    $('#loading').text("Se incarca...");
    $.ajax({
        type: 'POST',
        url: '/smooth_image',
        success: function(resp){
            $('#display_image').attr('src',resp.image_url_smooth + "?a=" + performance.now());
            $('#loading').text("");
        },
    });
});