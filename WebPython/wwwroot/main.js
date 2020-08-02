import { html, render } from 'https://unpkg.com/lit-html?module';
//import {} from https://unpkg.com/material-components-web@7.0.0/dist/material-components-web.js?module
import { ajax_submit_calculate_area, ajax_submit_calculate_area_and_comment } from './lib.js'

window.addEventListener("load", function () {

    [].map.call(document.querySelectorAll('.mdc-text-field'), function (el) {
        return new mdc.textField.MDCTextField(el);
    });

    [].map.call(document.querySelectorAll('.mdc-button'), function (el) {
        return new mdc.ripple.MDCRipple(el);
    });

    [].map.call(document.querySelectorAll('.mdc-button'), function (el) {
        return new mdc.ripple.MDCRipple(el);
    });

    let btn_area = document.getElementById('bt_calculate_area');
    btn_area.addEventListener('click', (event) => {
        calculate_area(btn_area);
    });

    let btn_area_and_comment = document.getElementById('bt_calculate_area_and_comment');
    btn_area_and_comment.addEventListener('click', (event) => {
        calculate_area_and_comment(btn_area_and_comment);
    });
        
});


async function calculate_area_and_comment(btn) {
    btn.disabled = true;
    let width = document.getElementById("input_width").value;
    let height = document.getElementById("input_height").value;
    var response = await ajax_submit_calculate_area_and_comment(width, height);
    btn.disabled = false;
    renderResponse(response);
}

async function calculate_area(btn) {
    btn.disabled = true;
    let width = document.getElementById("input_width").value;
    let height = document.getElementById("input_height").value;
    var response = await ajax_submit_calculate_area(width, height);
    btn.disabled = false;
    renderResponse(response);
}

const areaResultTemplate = (result) => html`<label>Result: <span>${result}</span></label>`;
const areaResultWithCommentTemplate = (result) => html`<label>Result:<span>${result.value}</span> Comment:<span>${result.comment}</span> </label>`;
const errorTemplate = (error, url) => html`<span>${error} - ${url}</span>`;

const renderResult = (result) => result.comment ?
    render(areaResultWithCommentTemplate(result), document.getElementById("data_result_container")) :
    render(areaResultTemplate(result), document.getElementById("data_result_container"));

const renderError = (error, url) => render(errorTemplate(error, url), document.getElementById("data_result_container") )

const renderResponse = (response) => response.success ?
    renderResult(response.result) :
    renderError( response.error, response.url);