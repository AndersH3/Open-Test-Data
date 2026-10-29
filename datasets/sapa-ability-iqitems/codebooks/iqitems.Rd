\name{iqitems}
\alias{iqitems}
\docType{data}
\title{16 multiple choice IQ items}
\description{16 multiple choice ability items taken from  the Synthetic Aperture Personality Assessment (SAPA) web based personality assessment project.  The data from 1525 subjects are included here as a demonstration set for scoring multiple choice inventories and doing basic item statistics. For more information on the development of an open source measure of cognitive ability, consult the readings available at the \url{https://personality-project.org/}.  
}
\usage{data(iqitems)}
\format{
   A data frame with 1525 observations on the following 16 variables. The number following the name is the item number from SAPA.
  \describe{
    \item{\code{reason.4}}{Basic reasoning questions }
    \item{\code{reason.16}}{Basic reasoning question}
    \item{\code{reason.17}}{Basic reasoning question}
    \item{\code{reason.19}}{Basic reasoning question }   
     \item{\code{letter.7}}{In the following alphanumeric series, what letter comes next?}
    \item{\code{letter.33}}{In the following alphanumeric series, what letter comes next?}
    \item{\code{letter.34}}{In the following alphanumeric series, what letter comes next}
    \item{\code{letter.58}}{In the following alphanumeric series, what letter comes next?}
    \item{\code{matrix.45}}{A matrix reasoning task}
    \item{\code{matrix.46}}{A matrix reasoning task}
    \item{\code{matrix.47}}{A matrix reasoning task}
    \item{\code{matrix.55}}{A matrix reasoning task}
    \item{\code{rotate.3}}{Spatial Rotation of type 1.2}
    \item{\code{rotate.4}}{Spatial Rotation of type 1.2}
     \item{\code{rotate.6}}{Spatial Rotation of type 1.1}
    \item{\code{rotate.8}}{Spatial Rotation of type 2.3}
  }
}
\details{16 items were sampled from 80 items given as part of the SAPA (\url{https://www.sapa-project.org/}) project  (Revelle, Wilt and Rosenthal, 2009; Condon and Revelle, 2014) to develop online measures of ability. These 16 items reflect four lower order factors (verbal reasoning, letter series, matrix reasoning, and spatial rotations.  These lower level factors all share a higher level factor ('g'). Similar data are available from the International Cognitive Abiity Resource at \url{https://www.icar-project.org/} .

This data set and the associated data set (\code{\link{ability}} based upon scoring these multiple choice items and converting them to correct/incorrect may be used to demonstrate item response functions, \code{\link[psych]{tetrachoric}} correlations, or \code{\link[psych]{irt.fa}} 
 as well as \code{\link[psych]{omega}} estimates of of reliability and hierarchical structure.

In addition, the data set is a good example of doing item analysis to examine the empirical response probabilities
 of each item alternative as a function of the underlying latent trait.  When doing this, 
 it appears that two of the matrix reasoning problems do not have monotonically increasing trace lines for the probability correct. 
  At moderately high ability (theta = 1) there is a decrease in the probability correct from theta = 0 and theta = 2.
}
\source{ The example data set is taken from the Synthetic Aperture Personality Assessment personality and ability test at \url{https://www.sapa-project.org/}.  The data were collected with David Condon from 8/08/12 to 8/31/12.
} 

\references{

Condon, David and Revelle, William, (2014) The International Cognitive Ability Resource:  Development and initial validation of a public-domain measure. Intelligence, 43, 52-64.

Revelle, William, Dworak, Elizabeth M. and Condon, David (2020) Cognitive ability in everyday life: the utility of open-source measures.  Current Directions in Psychological Science, 29, (4) 358-363. Open access at \doi{10.1177/0963721420922178}.

Dworak, Elizabeth M., Revelle, William, Doebler, Philip and Condon, David (2021)  Using the International Cognitive Ability Resource as an open source tool to explore individual differences in cognitive ability.  Personality and Individual Differences, 169. Open access at \doi{10.1016/j.paid.2020.109906}.


Revelle, W., Wilt, J.,  and Rosenthal, A. (2010)  Individual Differences in Cognition: New Methods for examining the Personality-Cognition Link In Gruszka, A.  and Matthews, G. and Szymura, B. (Eds.) Handbook of Individual Differences in Cognition: Attention, Memory and Executive Control, Springer.

 Revelle, W,  Condon, D.M.,  Wilt, J.,  French, J.A., Brown, A.,  and  Elleman, L.G. (2016) Web and phone based data collection using planned missing designs. In  Fielding, N.G.,  Lee, R.M. and  Blank, G. (Eds). SAGE Handbook of Online Research Methods (2nd Ed), Sage Publcations.
 }
\examples{
\donttest{
data(iqitems)
iq.keys <- c(4,4,4, 6,  6,3,4,4,   5,2,2,4,   3,2,6,7)
psych::score.multiple.choice(iq.keys,iqitems)   #this just gives summary statisics
#convert them to true false 
iq.scrub <- psych::scrub(iqitems,isvalue=0)  #first get rid of the zero responses
iq.tf <-  psych::score.multiple.choice(iq.keys,iq.scrub,score=FALSE) 
              #convert to wrong (0) and correct (1) for analysis
psych::describe(iq.tf) 
#see the ability data set for these analyses
#now, for some item analysis
iq.irt <- psych::irt.fa(iq.tf)  #do a basic irt
iq.sc <- psych::scoreIrt(iq.irt,iq.tf)  #find the scores
op <- par(mfrow=c(4,4))
psych::irt.responses(iq.sc[,1], iq.tf)  
op <- par(mfrow=c(1,1))
}
}
\keyword{datasets}
