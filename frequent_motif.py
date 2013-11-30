#Problem 1, Frequent Words
#goes through text string s and creates substring motifs length integer k
#with each motif
#tests how many times each substring occurs in string s
#returns a list of all most frequent k-mers in text
#if there is a tie, all substrings are returned
import collections


def motif_counter(s,t):
   motif_dict={}
   s_len=len(s)
   high_freq=1
   for position in range(s_len):
      if position+t<=s_len:
         motif1=s[position:position+t]
         freq=1
         for position2 in range(position+1,s_len):
            if position2+t<=s_len:
               motif2=s[position2:position2+t]
               if motif1==motif2:
                  freq+=1
                  if freq>=high_freq:
                     high_freq+=1
                     if high_freq not in motif_dict:
                        motif_dict[high_freq]=[motif2]
                     else:
                        motif_dict[high_freq].append(motif2)
      high_freq=1
   sorted_occurences=sorted(motif_dict.keys())
   highest_occurence=sorted_occurences[-1]
   high_motif_list=motif_dict[highest_occurence]
   return high_motif_list

s='ACTAAAAACTAAAAATGGAGTGCCGTCTGTCTCCTGTCTCAGCTTGGTGCCGTCTGTCTCCTGTCTCGTGCCGTGTGCCGTAGCTTGGTGCCGTCTGTCTCCTGTCTCACTAAAAAGCTTGATGGAATGGAACTAAAAGTGCCGTAGCTTGATGGAACTAAAACTGTCTCGTGCCGTCTGTCTCAGCTTGACTAAAACTGTCTCAGCTTGGTGCCGTACTAAAAGTGCCGTATGGAAGCTTGCTGTCTCCTGTCTCACTAAAAGTGCCGTAGCTTGCTGTCTCCTGTCTCAGCTTGCTGTCTCACTAAAACTGTCTCACTAAAAATGGAGTGCCGTAGCTTGAGCTTGACTAAAACTGTCTCACTAAAACTGTCTCATGGACTGTCTCCTGTCTCATGGAGTGCCGTGTGCCGTGTGCCGTGTGCCGTGTGCCGTCTGTCTCACTAAAAATGGAATGGAGTGCCGTACTAAAAATGGACTGTCTCGTGCCGTGTGCCGTCTGTCTCCTGTCTCACTAAAAAGCTTGGTGCCGTCTGTCTCAGCTTGACTAAAAGTGCCGTAGCTTGGTGCCGTCTGTCTCATGGAGTGCCGTAGCTTGAGCTTGCTGTCTCATGGAAGCTTGCTGTCTCATGGAAGCTTGGTGCCGTGTGCCGTAGCTTGAGCTTGGTGCCGTACTAAAAGTGCCGTATGGAGTGCCGTACTAAAAAGCTTGAGCTTGACTAAAAGTGCCGTCTGTCTCAGCTTGACTAAAAAGCTTGACTAAAAAGCTTGGTGCCGTACTAAAAAGCTTGCTGTCTCATGGAATGGAAGCTTGCTGTCTCCTGTCTCCTGTCTCCTGTCTCATGGAATGGAAGCTTGATGGAATGGA'
t=12
new_list=str(motif_counter(s,t)).strip('[]')
new_list1=new_list.replace(',','')
new_list2=new_list1.replace("'",'')
print(new_list2)
