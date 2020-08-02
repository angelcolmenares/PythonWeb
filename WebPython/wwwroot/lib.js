
export const ajax_submit_calculate_area = async (width, height) =>
{
    let url = "api/pythoncalculator/calculate-area?width=" + width + "&height=" + height;
    return await ajax_submit_get(url, "text");
}


export const ajax_submit_calculate_area_and_comment = async (width, height)=> {
    let url = "api/pythoncalculator/calculate-area-and-comment?width=" + width + "&height=" + height;
    return await ajax_submit_get(url, "json");
}

async function ajax_submit_get(url, reponseType) {

    try {
        const response = await fetch(url, {
            method: 'GET'
        });

        if (response.ok) {
            var result = reponseType == "json" ? await response.json() : await response.text();
            return { success: true, result: result };
        }
        else {
            console.log(response)
            return { success: false, error: `${response.status}-${response.statusText}`, url: response.url }
        };

    } catch (error) {
        console.error('Error:', error);
        return { success: false, error: error, url: url };
    }
}


