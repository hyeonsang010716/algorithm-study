import requests
from bs4 import BeautifulSoup


base = 'https://www.acmicpc.net/problem/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}

def get_data(num):
    url = base + str(num)

    response = requests.get(url,headers=headers)

    print(response)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        problem_description = soup.select('#problem_description > p')
        problem_ul = soup.select('#problem_description > ul')
        input_description = soup.select('#problem_input > p')
        output_description = soup.select('#problem_output > p')
        sample_input = soup.select_one('#sampleinput1').text.strip()
        sample_output = soup.select_one('#sampleoutput1').text.strip()
        sample_i = soup.select("pre[id^=sample-input]")
        sample_o = soup.select("pre[id^=sample-output]")

        content = ""

        for description in problem_description:
            content += description.text.strip() + '\n\n' 

        for ul in problem_ul:
            content += ul.text.strip() + '\n\n' 

        content += "IN" + '\n'

        for in_description in input_description:

            content += in_description.text.strip() + '\n\n'

        content += "OUT" + '\n'

        for out_description in output_description:
            content += out_description.text.strip() + '\n\n'

        inputs = []

        outputs = []

        for i in range(len(sample_i)):
            inputs.append(sample_i[i].text.strip())
            outputs.append(sample_o[i].text.strip())

        return True , content , inputs , outputs

    else:
        return False , None , None , None


if __name__ == "__main__":
    get_data(1000)