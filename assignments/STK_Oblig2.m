% Oppgave 2 D
%n_values = [3, 10, 30];
%for i = 1:3
%n = n_values(i);
n = 3;
X = unifrnd(0, 1, n, 10000);
Y = exprnd(1, n, 10000);
Z = binornd(1, 0.5, n, 10000);
meanX = mean(X);
meanY = mean(Y);
meanZ = mean(Z);

mu_uni = 1/2;
sigma_uni = 1/(2*sqrt(3));
mu_exp = 1;
sigma_exp = 1;
mu_ber = 1/2;
sigma_ber = 1/2;
Z1 = sqrt(n)*(meanX - mu_uni) / sigma_uni;
Z2 = sqrt(n)*(meanY - mu_exp) / sigma_exp;
Z3 = sqrt(n)*(meanZ - mu_ber) / sigma_ber;

%subplot(3,1,i);
hist(Z1, -3:0.25:3);
title(['Uniform distribution: n = ', num2str(n)]);
%end
%subplot(3,1,2);
%hist(Z2, -3:0.25:3);
%title('Exponential Distribution')
%subplot(3,1,3);
%hist(Z3, -3:0.25:3);
%title('Bernoulli Distribution')

%Oppgave 2 F
int = [-Inf, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, Inf]
ant_uni = histc(Z1, int);
%ant_exp = histc(Z2, int);
%ant_ber = histc(Z3, int);

rekv_uni = ant_uni(1:12)/10000
%rekv_exp = ant_exp(1:12)/10000
%rekv_ber = ant_ber(1:12)/10000

%subplot(3,1,1);
%hist(rekv_uni, -3:0.25:3);
%title('Uniform Distribution')
%subplot(3,1,2);
%hist(rekv_exp, -3:0.25:3);
%title('Exponential Distribution')
%subplot(3,1,3);
%hist(rekv_ber, -3:0.25:3);
%title('Bernoulli Distribution')
