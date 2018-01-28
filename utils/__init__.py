
import re



def get_song_detail(song_id, refresh_html=False):
    """
    song_id에 해당하는 곡 정보 dict를 반환
    위의 get_top100_list의 각 곡 정보에도 song_id가 들어가도록 추가
    http://www.melon.com/song/detail.htm?songId=30755375
    위 링크를 참조
    파일명
        song_detail_{song_id}.html
    :param song_id: Melon사이트에서 사용하는 곡의 고유 ID값
    :param refresh_html: 이미 다운받은 HTML데이터가 있을 때 기존 데이터를 덮어씌울지 여부
    :return: 곡 정보 dict
    """
    # 파일위치는 data/song_detail_{song_id}.html

def search_song(q):
    """
    곡 명으로 멜론에서 검색한 결과 리스트를 리턴
    :param q: 검색할 곡 명
    :return: 결과 dict리스트
    """
    """
    1. http://www.melon.com/search/song/index.htm
        에 q={q}, section=song으로 parameter를 준 URL에
        requests를 사용해 요청
    2. response.text를 사용해 BeautifulSoup인스턴스 soup생성
    3. soup에서 적절히 결과를 가공
    4. 결과 1개당 dict한개씩 구성
    5. 전부 리스트에 넣어 반환
    6. 완☆성
    """
    url = 'https://www.melon.com/search/song/index.htm'
    params = {
        'q': q,
        'section': 'song',
    }
    response = requests.get(url, params)
    soup = BeautifulSoup(response.text, 'lxml')
    tr_list = soup.select('form#frm_defaultList table > tbody > tr')
    # tr_list = soup.find('form', id='frm_defaultList').find('table').find('tbody').find_all('tr')

    result = []
    for tr in tr_list:
        title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
        artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
            strip=True)
        album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

        result.append({
            'title': title,
            'artist': artist,
            'album': album,
        })
    return result