#coding:utf-8
import pandas as pd
from scipy import stats

df = pd.read_csv('C:\\Users\xxx\Downloads\\xxx.csv') #记得改路径
use_time_base = df[df['exp'].dropna().str.contains("对照")]['use_time']/60
use_time_exp = df[df['exp'].dropna().str.contains("实验")]['use_time']/60

print('【use_time样本概况】')
mean_base = use_time_base.mean()
std_base = use_time_base.std()
mean_exp = use_time_exp.mean()
std_exp = use_time_exp.std()
print("对照组：样本均值为%.2f，样本标准差为%.2f" % (mean_base,std_base))
print("实验组：样本均值为%.2f，样本标准差为%.2f" % (mean_exp,std_exp))
if stats.kstest(use_time_base, 'norm', (mean_base, std_base))[1] < 0.05 and stats.kstest(use_time_exp, 'norm', (mean_exp, std_exp))[1] < 0.05:
    print("对照组服从正态分布：",stats.kstest(use_time_base, 'norm', (mean_base, std_base)))
    print("实验组服从正态分布：", stats.kstest(use_time_exp, 'norm', (mean_exp, std_exp)))
    if stats.levene(use_time_base, use_time_exp)[1] > 0.05:
        print("对照组和实验组方差相等：", stats.levene(use_time_base, use_time_exp))
        if stats.ttest_ind(use_time_base,use_time_exp)[1] < 0.05:
            print("T检验结论：对照组和实验组存在显著差异",stats.ttest_ind(use_time_base,use_time_exp))
        else:
            print("T检验结论：对照组和实验组不存在显著差异",stats.ttest_ind(use_time_base,use_time_exp))
    else:
        print("对照组和实验组方差不相等：", stats.levene(use_time_base, use_time_exp))
        if stats.ttest_ind(use_time_base,use_time_exp,equal_var=False)[1] < 0.05:
            print("T检验结论：对照组和实验组存在显著差异",stats.ttest_ind(use_time_base,use_time_exp,equal_var=False))
        else:
            print("T检验结论：对照组和实验组不存在显著差异",stats.ttest_ind(use_time_base,use_time_exp,equal_var=False))
        if stats.mannwhitneyu(use_time_base, use_time_exp, alternative='two-sided')[1] < 0.05:
            print("非参数检验结论：对照组和实验组存在显著差异",stats.mannwhitneyu(use_time_base, use_time_exp, alternative='two-sided'))
        else:
            print("非参数检验结论：对照组和实验组不存在显著差异",stats.mannwhitneyu(use_time_base, use_time_exp, alternative='two-sided'))
else:
    print("样本数据不服从正态分布，进行非参数检验：",stats.mannwhitneyu(use_time_base, use_time_exp, alternative='two-sided'))
    if stats.mannwhitneyu(use_time_base, use_time_exp, alternative='two-sided')[1] < 0.05:
        print("非参数检验结论：对照组和实验组存在显著差异")
    else:
        print("非参数检验结论：对照组和实验组不存在显著差异")
