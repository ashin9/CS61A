"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime
import string

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # 列表生成式由 select 筛选生成新 list, 然后再选择第 k 个 list 元素
    selected = [x for x in paragraphs if select(x)]
    if k >= len(selected):
        return ''
    else:
        return selected[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def topic_in(paragraph):
        # 创建翻译表, 将标点符号映射为 None
        translator = str.maketrans('', '', string.punctuation)
        # 去除标点符号
        paragraph = paragraph.translate(translator)
        # 转为小写, 并分割字符串
        paragraph = lower(paragraph).split()

        # 遍历判断
        for item in topic:
            if item in paragraph:
                return True
        return False
    return topic_in
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # 特殊情况判断
    if len(typed_words) == 0:
        return 0.0
    # 正常挨个匹配
    match_num = 0
    for i in range(min(len(typed_words),len(reference_words))):
        if typed_words[i] == reference_words[i]:
            match_num = match_num + 1
    return (match_num / len(typed_words)) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5.0 * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 首先考虑特殊情况
    if user_word in valid_words:
        return user_word
    # 每个 valid_word 计算 diff, 选 diff 最小的
    diff_list = [diff_function(user_word, word, limit) for word in valid_words]
    if min(diff_list) > limit:
        return user_word
    else:
        return valid_words[diff_list.index(min(diff_list))]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    # 递归边界
    if start == '' or goal == '':
        return abs(len(goal)-len(start))
    # 递归体
    if start[0] == goal[0]:
        return 0 + shifty_shifts(start[1:], goal[1:], limit)
    else:
        # 控制最多 limit + 1
        if limit == 0:
            return 1
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    if start == '' or goal == '': # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return abs(len(goal)-len(start))
        # END

    elif start[0] == goal[0]: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0 + pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        if limit == 0:
            return 1
        
        add_diff = 1 + pawssible_patches(start, goal[1:], limit-1)
        remove_diff = 1 + pawssible_patches(start[1:], goal, limit-1)
        substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit-1)
        
        # 直接每种情况都跑, 取最小的
        return min(min(add_diff, remove_diff), substitute_diff)
    
        # 很难判断什么时候 add, remove, substitute
        # if start[0] != goal[0] and len(start) == 1:
        #     substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit-1)
        #     return substitute_diff
    
        # if start[0] == goal[1]:
        #     add_diff = 1 + pawssible_patches(start, goal[1:], limit-1) # Fill in these lines
        #     return add_diff
        
        # elif start[1] == goal[0]:
        #     remove_diff = 1 + pawssible_patches(start[1:], goal, limit-1)
        #     return remove_diff
        # else:
        #     substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit-1)
        #     return substitute_diff
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    match = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            match = match + 1
        else:
            break
    progress = match / len(prompt)

    send({'id':user_id, 'progress': progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for player in times_per_player:
        times.append([player[i+1]-player[i] for i in range(len(player)-1)])
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    fastest = [[] for i in player_indices]
    # 遍历 word
    for word_index in word_indices:
        # 时间列式列表
        word_times = [all_times(game)[player][word_index] for player in player_indices]
        # 最小时间索引
        min_index = min(player_indices, key = lambda x: word_times[x])
        # 添加对应 word 到 player
        fastest[min_index].append(word_at(game,word_index))
    return fastest

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)