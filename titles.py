
import scrap_job

def get_titles():
    df = scrap_job.scrap()
    titles_lst = df['Title'].tolist()
    return titles_lst

if __name__ == '__main__':
    print(get_titles())