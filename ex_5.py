



def GenerateBBSTArray(a):

    def _get_size(array_len, current_len, current_depth):
        # print('cl', current_len)
        if current_len < array_len:
            current_len += 2 ** current_depth
            current_len = _get_size(array_len, current_len, current_depth + 1)
        if current_len >= array_len:
            return current_len

    # def _get_size(self, size, depth, need):
    #     lvl_size = 2 ** depth + size
    #     if depth > 0:
    #         lvl_size = self._get_size(lvl_size, depth - 1)
    #     return lvl_size

    def _get_leftchild_of(idx):
        return 2 * idx + 1
    
    def _get_rightchild_of(idx):
        return 2 * idx + 2

    def _GenerateBBSTArray(bsta, array, child_idx):
        center = len(array)//2

        if len(array) == 0:
            return

        bsta[child_idx] = array[center]
        left_child_idx = _get_leftchild_of(child_idx)
        if left_child_idx <= len(bsta):
            _GenerateBBSTArray(bsta, array[:center], left_child_idx)


        right_child_idx = _get_rightchild_of(child_idx)
        if right_child_idx <= len(bsta):
            _GenerateBBSTArray(bsta, array[center+1 : ], right_child_idx)
        
    tmp = sorted(a)
    bsta = [None] * _get_size(len(tmp), 0, 0)
    _GenerateBBSTArray(bsta, tmp, 0)
    return bsta
