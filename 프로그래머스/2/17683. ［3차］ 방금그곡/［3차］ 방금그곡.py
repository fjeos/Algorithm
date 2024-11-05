def solution(m, musicinfos):
    answer = []
    dic = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b'}
    for music in musicinfos:
        start_time, end_time, title, codes = music.split(",")
        start_min, start_sec = map(int, start_time.split(":"))
        end_min, end_sec = map(int, end_time.split(":"))

        run_time = (end_min * 60 + end_sec) - (start_min * 60 + start_sec)

        for key, value in dic.items():
            if key in codes:
                codes = codes.replace(key, value)
            if key in m:
                m = m.replace(key, value)

        repeated_codes = (codes * (run_time // len(codes) + 1))[:run_time]

        if m in repeated_codes:
            answer.append([title, run_time])


    return sorted(answer, key=lambda x: -x[1])[0][0] if answer else '(None)'