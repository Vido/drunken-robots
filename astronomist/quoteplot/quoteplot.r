stock.df = read.csv("table.csv", header = TRUE, stringsAsFactors = FALSE)
stock.ts = ts(data=stock.df$Adj.Close, frequency=252, start=c(2000, 1), end=c(2014, 1))
plot(stock.ts, col="blue", lwd=2, ylab="Adjusted close")
abline(lsfit(stock.ts, stock.ts))
