


def find_two_sum(nums, target):
    # دیکشنری برای ذخیره مقادیر و اندیس‌های مربوط به آنها
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        # بررسی اینکه آیا عدد مکمل قبلاً دیده شده است
        if complement in num_dict:
            return (num, complement)  # بازگشت دو عدد
        num_dict[num] = i
    return None  # اگر جوابی پیدا نشد

# مثال استفاده
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum(nums, target)
if result:
    print("دو عدد مورد نظر:", result)
else:
    print("هیچ جفتی یافت نشد.")









def find_two_sum_sorted(nums, target):
    nums.sort()  # مرتب‌سازی لیست
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left], nums[right])  # جفت مناسب
        elif current_sum < target:
            left += 1  # افزایش اشاره‌گر سمت چپ
        else:
            right -= 1  # کاهش اشاره‌گر سمت راست
    return None  # اگر جفتی یافت نشد


# مثال استفاده
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum_sorted(nums, target)
if result:
    print("دو عدد مورد نظر:", result)
else:
    print("هیچ جفتی یافت نشد.")

