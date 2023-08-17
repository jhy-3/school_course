Market traders buy and sell volatile assets frequently, with a goal to maximize their total return. ==交易员==总是希望能够通过预测资产涨停情况来提高自己的收益，并且尽可能减少投资时的风险（收益降低甚至破产）。黄金和比特币是两种具有代表性的资产。本文通过附件数据预测可能最佳投资方案，将后悔度作为证据验证策略，调整佣金检验方案对成本的灵敏度，将决策与结果作为备忘录写给the trader。

1本文引入多阶段模糊投资方法，通过分析黄金和比特币的特性，决定分阶段投资，投资的决策依据主要来自交易日之前的价格数据（附表LBMA-GOLD.csv,BCHAIN-MKPRU.csv）,每次投资改变或者维持当前资产比例（C,G,B），以达到降低损失提高收益的目的，得出结果：在 9/11/2016投资1000美金将会在 9/10/2021收获62211美金，最终比例是0 64 936

2为了确保证据具有说服力，这里将后悔度作为可靠的评价证据。我们将手持的三种资产进行风险划分（比特币：黄金：美金：），绘制风险收益比-后悔度曲线。将采用决策的后悔度和三种极端情况比较（全部购置黄金，全部购置比特币，黄金：比特币=1：1），得出结论：无论是何种收益风险比例，模型做出的决策的后悔度始终处在一个低水平（0.2-0.5），较低的后悔度反应决策的合理性。

3成本的调整会导致收益的改变，这反映策略对成本的敏感程度。本题中成本就是佣金（最开始是gold = 1% , bitcoin = 2%）。因此，我们调整佣金比例，分别降低成（gold = 0.1% , bitcoin = 0.2%  gold = 0.01% , bitcoin = 0.02%），得出结论：交易成本的降低，让前期决策获得更高的收益，投资的比特币占比得到提高，最终财富也得到小幅度提升。（62211->63157->63874）

**==α变成γ==**

Last but not least, we summarize the suggestions and write a memorandum to the trader to communicate our strategy, model, and results,hoping(xxxxx待修改完善)

The adjustment of costs leads to a change in returns, which reflects the sensitivity of the strategy to costs. The cost in this case is the commission (initially gold = 1% , bitcoin = 2%). Therefore, we adjust the commission percentage and reduce it to (gold = 0.1% , bitcoin = 0.2% gold = 0.01% , bitcoin = 0.02%) respectively, concluding that the reduction in transaction costs results in higher returns on the upfront decisions, an increase in the percentage of bitcoins invested, and a small increase in the final wealth.



```markdown
	Market traders buy and sell volatile assets frequently, with a goal to maximize their total return. Traders are always looking to increase their returns by predicting asset ups and downs and minimizing the risk (lower returns or even bankruptcy) when investing. Gold and Bitcoin are two representative assets. In this paper, we use the attached data to predict the possible best investment scenarios, use the regret value as evidence to validate the strategy, adjust the commission to test the sensitivity of the scenarios to the cost, and write the model decision as a memo to the trader.
	 In this paper,we introduce a multi-stage fuzzy investment method,.By analyzing the characteristics of gold and bitcoin, we decide to invest in stages, the investment decision is mainly based on the price data before the trading day (schedule LBMA-GOLD.csv, BCHAIN-MKPRU.csv), each investment change or maintain the current asset ratio (C,G,B), in order to achieve the purpose of reducing losses and increasing returns The result: investing $1000 on 9/11/2016 will result in $62,211 on 9/10/2021, the final ratio is 0 64 931
	To ensure that the evidence is convincing, regret levels are used as reliable evaluation evidence. We divide the risk of the three assets in hand (bitcoin:high gold:mid cash:free) and plot the risk-return ratio-regret curve. The regret value of the adopted decision is compared with three extreme cases (all gold acquisition, all bitcoin acquisition, gold: bitcoin = 1:1).Here comes the conclusion: the regret level of the decisions made by the model is always at a low level (0.2-0.5), regardless of the return-risk ratio, and the lower regret value reflects the reasonableness of the decision.
	The adjustment of costs leads to a change in returns, which reflects the sensitivity of the strategy to costs. The cost in this case is the commission (initially γgold = 1% , γbitcoin = 2%). Therefore, we adjust the commission percentage and reduce it to (γgold = 0.1% , γbitcoin = 0.2% ;γgold = 0.01% , γbitcoin = 0.02%) respectively, concluding that the reduction in transaction costs results in higher returns on the upfront decisions, an increase in the percentage of bitcoins invested, and a small increase in the final wealth.(62211->63157->63874).
	Last but not least, we summarize the suggestions and write a memorandum to the trader to communicate our strategy, model, and results,hoping to bring a more perfect trading strategy.
	
Key Words 
```

