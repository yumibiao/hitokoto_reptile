#include <fstream>
#include <iostream>
#include <map>

using namespace std;

/*
struct node{
  string s;
  int cnt;
}nd[1000002];*/

map<string ,int> mp;

/*
bool cmp2(node a,node b){
  return a.cnt>b.cnt;
}*/

int main(){
  std::ofstream owo,pwp;
  std::ifstream ovo;
  ovo.open("data.txt");//open_file
  owo.open("data_out.txt");//out_file
 // pwp.open("an.txt");
  std::string tmp;
  while(getline(ovo,tmp)){
    //tmp=tmp;
    //cout<<tmp<<"\n";
    if(tmp=="")cout<<"what?\n";
    if(tmp=="")continue;
    if(!mp[tmp])owo<<tmp<<"\n";
    mp[tmp]++;
  }
  /*
  int cnt=0;
  for(map<string,int>::iterator it=mp.begin();it!=mp.end();it++){
    nd[++cnt].s=it->first;
    nd[cnt].cnt=it->second;
    //pwp<<  << "," << nd[cnt].c=it->second <<"\n";
    cnt++;
    //if(cnt>=200)break;
  }
  sort(nd+1,nd+cnt+1,cmp2);
  pwp<<cnt<<"\n";
  int cnt2=0;
  for(int i=1;i<=cnt;i++){
    pwp<<nd[i].s<<","<<nd[i].cnt<<"\n";
    cnt2+=nd[i].cnt;
  }
  pwp<<cnt2;*/
  ovo.close();
  owo.close();
}