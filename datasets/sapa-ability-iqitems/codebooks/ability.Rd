\name{ability}
\alias{ability}
\alias{ability.keys}
\docType{data}
\title{16 ability items scored as correct or incorrect.}
\description{
16 multiple choice ability items 1525 subjects taken from the Synthetic Aperture Personality Assessment (SAPA) web based personality assessment project are saved as \code{\link{iqitems}}. Those data are shown as examples of how to score multiple choice tests and analyses of response alternatives.  When scored correct or incorrect, the data are useful for demonstrations of  tetrachoric based factor analysis \code{\link[psych]{irt.fa}} and finding tetrachoric correlations. 
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
\details{16 items were sampled from 80 items given as part of the SAPA (\url{https://www.sapa-project.org/}) project  (Revelle, Wilt and Rosenthal, 2009; Condon and Revelle, 2014) to develop online measures of ability. These 16 items reflect four lower order factors (verbal reasoning, letter series, matrix reasoning, and spatial rotations.  These lower level factors all share a higher level factor ('g').  

This data set may be used to demonstrate item response functions, \code{\link[psych]{tetrachoric}} correlations, or \code{\link[psych]{irt.fa}} as well as
 \code{\link[psych]{omega}} estimates of of reliability and hierarchical structure.

In addition, the data set is a good example of doing item analysis to examine the empirical response probabilities of each item 
alternative as a function of the underlying latent trait.  When doing this, it appears that two of the matrix reasoning problems do not have
 monotonically increasing trace lines for the probability correct.  
 At moderately high ability (theta = 1) there is a decrease in the probability correct from theta = 0 and theta = 2.
}
\source{ The example data set is taken from the Synthetic Aperture Personality Assessment personality and ability test at \url{https://www.sapa-project.org/}. 
 The data were collected with David Condon from 8/08/12 to 8/31/12.

Similar data are available from the International Cognitive Ability Resource at \url{https://www.icar-project.org/}.
} 

\references{
Condon, David and Revelle, William, (2014) The International Cognitive Ability Resource:  Development and initial validation of a public-domain measure. Intelligence, 43, 52-64.

Revelle, William, Dworak, Elizabeth M. and Condon, David (2020) Cognitive ability in everyday life: the utility of open-source measures.  Current Directions in Psychological Science, 29, (4) 358-363. Open access at \doi{10.1177/0963721420922178}.

Dworak, Elizabeth M., Revelle, William, Doebler, Philip and Condon, David (2021)  Using the International Cognitive Ability Resource as an open source tool to explore individual differences in cognitive ability.  Personality and Individual Differences, 169. Open access at \doi{10.1016/j.paid.2020.109906}.
Revelle, William, Wilt, Joshua,  and Rosenthal, Allen (2010)  Personality and Cognition: The Personality-Cognition Link. In Gruszka, Alexandra  and Matthews, Gerald   and Szymura, Blazej (Eds.) Handbook of Individual Differences in Cognition: Attention, Memory and Executive Control, Springer. 

}
\examples{
data(ability)
cs<- psych::cs
keys <- list(ICAR16=colnames(ability),reasoning =  cs(reason.4,reason.16,reason.17,reason.19),
  letters=cs(letter.7, letter.33,letter.34,letter.58), 
  matrix=cs(matrix.45,matrix.46,matrix.47,matrix.55), 
  rotate=cs(rotate.3,rotate.4,rotate.6,rotate.8))
  psych::scoreOverlap(keys,ability)
\donttest{    #this next step takes a few seconds to run and demonstrates IRT approaches
     ability.irt <- psych::irt.fa(ability)
     ability.scores <- psych::scoreIrt(ability.irt,ability)
     ability.sub.scores <- psych::scoreIrt.2pl(keys,ability) #demonstrate irt scoring
}
#It is sometimes asked how to handle missing data when finding scores
#this next example compares 3 ways of scoring ability items from icar
#Just sum the items
#Sum the means for the items
#IRT score the items

total <- rowSums(ability, na.rm=TRUE)
 means  <- rowMeans(ability, na.rm=TRUE)
irt <- psych::scoreIrt(items=ability)[1]
 df <- data.frame(total, means,irt)
 psych:: pairs.panels(df)


}
\keyword{datasets}
