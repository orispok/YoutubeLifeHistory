import sys
from dataclasses import dataclass

import pandas as pd
from bs4 import BeautifulSoup


@dataclass
class HistorySummaryRow:
    name: str
    count: int
    href: str


def parse_html(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    divs = soup.find_all('div', {'class': 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'})
    res_dic = {}
    for div in divs:
        if len(div.contents) > 3:
            href = div.contents[1]["href"]
            if href not in res_dic:
                res_dic[href] = HistorySummaryRow(div.contents[1].text, 1, href)
            else:
                res_dic[href].count += 1
    rows = [vars(res) for res in res_dic.values()]
    df = pd.DataFrame(rows)
    # sort by count
    df = df.sort_values(by="count", ascending=False)
    df.to_csv(output_file, index=False)


def main(input_file, output_file):
    parse_html(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
