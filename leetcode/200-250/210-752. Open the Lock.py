# 752. Open the Lock
from collections import deque
class Solution:
    def openLock(self, deadends, target):
        d = set(deadends)
        queue = deque([target])
        moves = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == "0000":
                    return moves
                for i in range(len(cur)):
                    nexts = [
                        cur[:i] + str((int(cur[i]) + 1) % 10) +  cur[i+1:],
                        cur[:i] + str((int(cur[i]) - 1) if cur[i] != '0' else 9) +  cur[i+1:]
                    ]
                    for nxt in nexts:
                        if nxt not in d: 
                            queue.append(nxt)
                            d.add(nxt)
            moves += 1
        return -1
                
sol = Solution()
print(sol.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(sol.openLock(deadends = [], target = "0202"))
print(sol.openLock(deadends = ["8888"], target = "0009"))
print(sol.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))    
print(sol.openLock(["0000"], "8888"))
print(sol.openLock(["7867","6676","8687","7886","6768","8877","6767","6676","6666","7876","6688","6677","6877","7786","6778","6868","6868","7867","7668","7666","8868","7887","6788","7687","7788","7877","6867","6867","7876","8787","8878","6668","6878","6766","8667","8688","6788","7687","8887","8766","6867","8867","7866","7866","6686","7776","8687","7888","6777","6678","6678","6686","6677","7886","6876","8666","6667","7768","7688","7668","6786","7766","7867","8866","7887","6676","8776","6867","8888","6678","8687","6868","7888","8666","6678","6668","7678","7667","8786","8768","6766","8776","8677","7788","7868","7878","6786","6678","6876","7667","8866","8666","8768","8886","8787","8688","8766","8867","7886","6876","7776","7867","8668","7777","8888","7767","8778","8888","6876","8777","7877","8866","8668","8878","7678","8787","7788","8887","8667","7887","6686","8778","7768","8787","7677","6768","7877","7788","7768","6768","6786","7887","7768","6676","6777","8686","7867","8788","8887","8776","7677","8786","8678","7666","8776","7676","6767","8776","8888","8766","8876","7777","7677","6767","7878","7868","8677","7677","8788","6667","8866","8887","6686","6777","6676","8787","6788","8866","6767","8676","8868","8768","8888","7866","7877","7768","7686","7888","6666","6887","6787","7667","6676","8666","8886","8878","8678","8868","8888","8867","7878","7787","8776","7877","6788","8778","6768","8677","8678","6778","7888","6866","6768","6666","6887","8866","7676","7866","7876","7678","7686","8887","7676","6788","8787","6666","8866","6876","8676","8688","8887","7887","7777","8887","8688","6668","6686","6887","7677","6867","6786","6877","7788","6667","8778","8786","8767","7778","8867","8877","6668","8886","7888","7767","7666","8678","8668","8767","7666","6787","6886","8787","6886","8768","8767","8676","6767","8776","8768","8687","8778","7888","6768","7878","6668","7688","6687","7866","8878","6877","7667","8886","7876","6667","8877","7666","7668","7676","6888","6686","7666","7688","7666","6678","6676","7678","8788","7667","7767","8766","6867","8767","8676","8786","8667","6678","6778","8877","8788","6866","7687","6876","8878","8866","6788","6877","8768","8778","8778","8866","7866","7887","7878","8766","8778","7868","8787","6676","8668","7866","8787","8767","6876","8867","6688","6886","6668","6878","7866","8678","8867","7667","7878","8778","8777","7866","8878","7868","6876","7688","7677","7678","7777","8888","8776","8688","6878","8877","7678","7777","7878","6678","6688","6868","8876","6668","8877","8786","6688","8766","8887","6678","8886","8876","8888","8878","6786","7686","7867","7767","7888","8866","6876","7767","6687","6687","6688","6868","8668","6886","8686","7766","8777","8667","8886","7676","7768","6788","8688","7676","7686","8777","7886","7788","6666","7687","6676","6777","6866","6767","7787","7877","6777","6886","7877","7787","7787","8768","7787","8778","6766","7677","6788","6786","6767","8687","6687","8668","6876","6666","7676","8667","6688","6766","6677","7667","8668","8866","7686","8866","8687","8866","8768","7886","6877","8877","6676","6887","6788","8877","8887","8886","8887","6676","8867","6867","7768","8868","6668","7878","7887","8768","6876","7787","7876","8886","6778","7778","7687","6686","7787","8767","8668","7686","7678","8788","6687","8666","7877","6668","7686","6866","6888","8786","7778","7786","8787","6777","6867","7787","7777","6766","8666","6778","6867","8668","8667","7678","8668","7677","8787","6876","6668","7788","7688","7687","8778","8787","8688","8867"]
,"6776"))