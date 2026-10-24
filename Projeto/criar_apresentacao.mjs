import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const root=process.cwd();
process.env.RUNTIME_NODE_MODULES='C:/Users/dsadm/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const skill='C:/Users/dsadm/.codex/plugins/cache/openai-primary-runtime/presentations/26.1022.11436/skills/presentations';
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const build=path.join(root,'tmp/slides');
const navy='#17324D', teal='#157A85', ink='#233343', muted='#536575';
const font='Arial';
const p=Presentation.create({slideSize:{width:1280,height:720}});
const source='Fontes: Projeto_Manutencao_Industrial.ipynb e tabelas em resultados/, calculados sobre a base de manutenção indicada no enunciado do Prof. Me. Daniel Vieira. Base: https://drive.google.com/file/d/1yQ7P-mbRK3Gsh12ey6ahxk8szc6pOie1/view';
const roteiro=[];
function txt(s,t,x,y,w,h,size=28,color=ink,bold=false){
 const sh=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 sh.text=t;sh.text.style={typeface:font,fontSize:size,color,bold};return sh;
}
function slide(title,notes){
 const s=p.slides.add();s.background.fill='#FFFFFF';
 txt(s,title,70,48,1140,100,44,navy,true);
 txt(s,String(p.slides.items.length).padStart(2,'0'),1170,665,60,30,18,muted);
 s.speakerNotes.text=notes+'\n\n'+source;
 roteiro.push({title,notes});return s;
}
function table(s,values,y=180,width=1140,height=330,cols){
 const t=s.tables.add({rows:values.length,columns:values[0].length,left:70,top:y,width,height,values,columnWidths:cols});
 for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
  const cell=t.getCell(r,c);cell.fill=r===0?navy:r%2?'#F0F5F7':'#FFFFFF';
  cell.text.style={typeface:font,fontSize:24,bold:r===0,color:r===0?'#FFFFFF':ink};
 }
 return t;
}
function chart(s,categories,values,label,y=180,max=1){
 const c=s.charts.add('bar',{position:{left:70,top:y,width:1140,height:380},categories,
  series:[{name:label,values,fill:teal}],barOptions:{direction:'column',grouping:'clustered'},
  hasLegend:false,chartFill:'#FFFFFF',plotAreaFill:'#FFFFFF',
  dataLabels:{showValue:true,position:'outEnd',textStyle:{fontSize:20}},
  xAxis:{tickLabelPosition:'low',textStyle:{fontSize:20}},
  yAxis:{min:Math.min(...values)<0?-0.1:0,max,numberFormatCode:'0.00',textStyle:{fontSize:20},majorGridlines:{fill:'#DCE4E8',width:1}}});
 applyPresentationChartFont(c,{fontFamily:font});
 return c;
}

let s=slide('Análise de falhas em\nequipamentos industriais',
'Este trabalho analisa as condições de operação de cinco máquinas da S&M Industry Tech. O objetivo foi entender quais variáveis aparecem associadas às falhas e comparar modelos de classificação. A apresentação resume o caminho da preparação dos dados até as recomendações de manutenção. O foco é explicar os resultados encontrados, inclusive as limitações do classificador.');
txt(s,'Projeto de Data Science e Big Data',70,260,1100,60,32,teal);
txt(s,'Carlos Alexandre Duarte Pereira\nData Science & Big Data Aplicados na Indústria\nDisciplina: Data Science e Big Data\nProfessor: Me. Daniel Vieira\n24/10/2026',70,390,1130,220,27);

s=slide('Problema e objetivo',
'A empresa enfrenta paradas não planejadas e utiliza parte da manutenção de forma corretiva. A proposta foi investigar os dados que já existem para apoiar a compreensão das falhas. Cada linha representa uma observação de uma máquina. O alvo vale zero quando não existe falha registrada e um quando existe. Esse detalhe é importante porque o trabalho classifica a condição do registro. Para prever com antecedência, seria necessário definir, por exemplo, se a máquina falhará nas próximas horas e reorganizar a base.');
txt(s,'A empresa enfrenta paradas não planejadas de máquinas.',70,185,1120,90,34,navy,true);
txt(s,'Objetivo: identificar condições associadas às falhas e avaliar modelos de classificação.',70,315,1120,110,31);
txt(s,'Alvo: falha no próprio registro\n0 = sem falha     1 = com falha',70,500,1120,100,29,teal);

s=slide('Base de dados e qualidade',
'O arquivo original possui 5.050 linhas e oito colunas. Foram retiradas 50 duplicatas exatas, restando cinco mil registros. Depois dessa limpeza, cada sensor apresentou 50 valores ausentes. Nos classificadores, a mediana foi calculada apenas com os dados de treinamento, dentro do Pipeline. Os valores extremos foram mantidos porque a base não informa os limites físicos de operação. Uma temperatura de 278,84 graus exige investigação, mas a estatística sozinha não permite afirmar se é um defeito do sensor ou uma condição real.');
table(s,[['Verificação','Resultado'],['Base original','5.050 registros e 8 atributos'],['Duplicatas exatas','50 registros removidos'],['Base limpa','5.000 registros em cinco máquinas'],['Ausências após limpeza','50 em cada variável operacional'],['Falhas na base limpa','903 registros, equivalentes a 18,06%']],170,1140,370,[470,670]);
txt(s,'Período observado: 01/01/2026 a 11/02/2026',70,580,1140,50,26,muted);

s=slide('Variáveis associadas às falhas',
'O gráfico mostra a correlação de Pearson entre as medições e a coluna falha. Horas de operação teve o maior valor, aproximadamente 0,381, seguida por vibração, com 0,304. Temperatura e corrente também apresentaram associação positiva, porém mais fraca. A pressão ficou próxima de zero. As médias de horas e vibração foram maiores entre os registros com falha. Esses resultados apoiam o acompanhamento conjunto dos sensores, mas não provam que uma variável cause a falha nem permitem definir um limite automático de parada.');
chart(s,['Horas de operação','Vibração','Corrente','Temperatura','Pressão'],[0.381,0.304,0.163,0.112,-0.022],'Correlação',180,0.5);
txt(s,'Horas de operação e vibração apresentam as maiores associações lineares.',70,595,1140,65,26,navy);

s=slide('Treinamento e avaliação',
'A separação respeitou a ordem do tempo. Os três mil registros iniciais serviram para treino, os mil seguintes para validação e os mil finais para teste. A validação serviu para comparar Árvore de Decisão, Random Forest e Regressão Logística. O critério foi o F1 da classe falha porque ele combina precisão e recall. Depois da escolha, a Random Forest foi ajustada com treino e validação reunidos. O teste ficou reservado para a avaliação final. Essa separação evita escolher o modelo olhando diretamente o resultado que deve representar uma avaliação independente.');
table(s,[['Conjunto','Registros','Finalidade'],['Treino','3.000','Ajuste inicial dos modelos'],['Validação','1.000','Comparação e escolha pelo F1'],['Teste','1.000','Avaliação final do modelo escolhido']],180,1140,280,[270,220,650]);
txt(s,'Atributos: temperatura, vibração, pressão, corrente e horas de operação.',70,510,1140,80,27);
txt(s,'Preparação dentro do Pipeline, com mediana aprendida no treino.',70,605,1140,50,25,teal);

s=slide('Comparação dos classificadores',
'A Random Forest apresentou o maior F1 na validação, aproximadamente 0,332. A Regressão Logística ficou em 0,315 e a Árvore de Decisão em 0,208. O modelo de referência escolhe sempre a classe sem falha e tem F1 igual a zero para a classe falha. A acurácia da árvore e da regressão foi ligeiramente maior, mas elas não foram escolhidas porque o critério definido era o F1. Esse resultado mostra por que a comparação depende da métrica adequada ao objetivo do problema.');
chart(s,['Random Forest','Regressão Logística','Árvore de Decisão','Referência'],[0.332,0.315,0.208,0],'F1 na validação',180,0.45);
txt(s,'Critério de escolha: maior F1 da classe falha na validação.',70,595,1140,60,27,navy);

s=slide('Random Forest no teste',
'Depois do reajuste com treino e validação, a Random Forest atingiu acurácia de 82,50 por cento e precisão de 58,44 por cento no teste. O recall foi de apenas 23,94 por cento. Em termos simples, ela encontrou 45 das 188 falhas existentes. O F1 ficou em 0,340. A leitura principal é que a acurácia parece alta, mas o modelo deixa a maior parte das falhas passar. Por isso, o resultado ainda não sustenta usar esse classificador como único critério de alerta de manutenção.');
table(s,[['Métrica','Resultado'],['Acurácia','82,50%'],['Precisão','58,44%'],['Recall','23,94%'],['F1-score','0,340']],180,650,350,[390,260]);
txt(s,'45 de 188',790,235,410,90,55,teal,true);
txt(s,'falhas identificadas\nno conjunto de teste',790,340,410,120,30);
txt(s,'A baixa detecção de falhas limita o uso do modelo.',70,585,1140,60,29,navy,true);

s=slide('Erros e impacto na manutenção',
'Nesta tabela, as linhas representam a situação registrada e as colunas representam a previsão. O modelo acertou 780 registros sem falha e 45 com falha. Os 32 falsos positivos poderiam gerar inspeções desnecessárias. O problema principal está nos 143 falsos negativos: eram falhas, mas o modelo respondeu sem falha. Isso equivale a 76,06 por cento das falhas do teste. A classe majoritária sozinha teria 81,20 por cento de acurácia nesse conjunto. Assim, o ganho de acurácia do modelo foi pequeno. Não foram calculados custos porque a base não fornece esses valores.');
table(s,[['Situação observada','Previsão sem falha','Previsão com falha'],['Sem falha','780','32'],['Com falha','143','45']],180,1140,250,[440,350,350]);
txt(s,'143 falsos negativos: falhas que passaram sem identificação.',70,475,1140,80,30,navy,true);
txt(s,'32 falsos positivos: possíveis inspeções ou alarmes indevidos.',70,580,1140,65,27);

s=slide('Perfis operacionais com K-Means',
'O K-Means agrupou os dados sem receber a coluna falha. Foram comparadas quantidades de dois a seis grupos e a melhor silhueta ocorreu com três. O cluster zero apresentou menores médias de horas de operação e vibração e taxa de falha de 4,46 por cento. No cluster um, essas médias foram maiores e a taxa chegou a 31,95 por cento. O cluster dois reúne apenas 25 registros, com temperatura média de 208,28 graus. Esse grupo evidencia a influência dos extremos e precisa ser investigado. A silhueta de 0,224 indica sobreposição, então esses perfis não são categorias definitivas de risco.');
table(s,[['Cluster','Registros','Taxa de falha','Perfil observado'],['0','2.509','4,46%','Menores horas e vibração'],['1','2.466','31,95%','Maiores horas e vibração'],['2','25','12,00%','Temperatura média de 208,28 °C']],170,1140,300,[140,180,240,580]);
txt(s,'Silhueta: 0,224. Os grupos ainda apresentam sobreposição.',70,525,1140,60,28);
txt(s,'A falha participa somente da análise posterior dos perfis.',70,605,1140,45,25,teal);

s=slide('Processamento com PySpark',
'A etapa de PySpark repetiu operações de leitura, seleção, filtro e agrupamento. Foi possível contar registros, verificar ausências e calcular taxas de falha por máquina. As contagens e taxas coincidiram com o Pandas. O Spark rodou em modo local, com os recursos de uma máquina. Como a base tem cinco mil registros, o Pandas já era suficiente. A contribuição dessa etapa foi utilizar uma API que pode trabalhar de forma distribuída quando existe uma infraestrutura adequada e um volume maior de dados. O trabalho não mediu ganho de velocidade.');
txt(s,'Operações realizadas',70,180,1140,60,32,teal,true);
txt(s,'Leitura do CSV e inspeção do schema\nSeleção de colunas e filtro de registros com falha\nAgrupamentos por máquina, classe e dia',70,270,1140,190,30);
txt(s,'Pandas e Spark produziram as mesmas contagens e taxas por máquina.',70,505,1140,90,30,navy,true);
txt(s,'Execução local, sem medição de desempenho distribuído.',70,620,1140,45,25,muted);

s=slide('Recomendações para a manutenção',
'As primeiras recomendações estão ligadas à qualidade da coleta. Os sensores com ausências e as temperaturas extremas precisam ser verificados. Outra ação é acompanhar horas de operação e vibração junto com as outras medições, pois esses atributos apareceram associados às falhas. A M04 merece investigação do histórico, mas sua taxa não autoriza concluir que seja a pior máquina. Para o modelo, ajustes de pesos das classes e do limite de decisão são possibilidades futuras, ainda não testadas. Esses ajustes precisam usar os dados de desenvolvimento e depois passar por avaliação em um novo período. Também é importante registrar as causas das falhas e as intervenções.');
table(s,[['Evidência','Ação proposta'],['Ausências e temperaturas extremas','Conferir coleta e calibração dos sensores'],['Horas e vibração associadas à falha','Acompanhar as medições em conjunto'],['M04 com taxa de 18,90%','Investigar histórico e condições de uso'],['Recall de 23,94%','Desenvolver o modelo e validar em novos dados'],['Histórico curto e poucos equipamentos','Ampliar a coleta e registrar intervenções']],165,1140,410,[510,630]);
txt(s,'As ações são propostas. O projeto não mediu redução de custos ou paradas.',70,610,1140,50,24,muted);

s=slide('Conclusões e limitações',
'O estudo encontrou associações úteis para orientar a investigação das falhas, principalmente envolvendo horas de operação e vibração. A classificação apresentou uma limitação clara: o modelo escolhido encontrou menos de um quarto das falhas no teste. Os agrupamentos ajudaram a descrever perfis, mas a sobreposição e os extremos exigem cuidado. O histórico contém cinco máquinas e aproximadamente seis semanas, sem limites técnicos completos dos equipamentos. O próximo passo é melhorar a qualidade da base e ampliar a avaliação com períodos novos. Para manutenção preditiva com antecedência, seria necessário definir outro alvo. A principal contribuição do trabalho foi transformar os registros em evidências para apoiar a análise da manutenção e mostrar os limites do que os modelos conseguiram identificar.');
txt(s,'Horas de operação e vibração se destacaram na análise das falhas.',70,185,1140,100,34,navy,true);
txt(s,'A Random Forest encontrou 23,94% das falhas do teste.\nA classificação exige melhoria e nova validação.',70,330,1140,130,31);
txt(s,'Limitações: cinco máquinas, cerca de seis semanas e ausência de limites técnicos completos.',70,500,1140,100,28);
txt(s,'Próximo passo: melhorar a coleta e avaliar novos períodos.',70,625,1140,45,27,teal,true);

await fs.mkdir(build,{recursive:true});
let md='# Roteiro de apresentação\n\n**Aluno:** Carlos Alexandre Duarte Pereira  \n**Disciplina:** Data Science e Big Data  \n**Duração sugerida:** 10 a 12 minutos\n\n';
roteiro.forEach((r,i)=>{md+=`## Slide ${i+1} — ${r.title.replaceAll('\n',' ')}\n\n${r.notes}\n\n`;});
md+='## Perguntas para discussão\n\n### Por que a acurácia alta não foi suficiente?\n\nA classe sem falha é majoritária. No teste, responder sempre sem falha já teria 81,20% de acurácia. O recall mostrou que o modelo encontrou somente 45 das 188 falhas.\n\n### Por que não remover todos os outliers?\n\nValores extremos podem ser sinais reais de falha. Sem os limites técnicos do equipamento, a exclusão automática poderia retirar informação importante.\n\n### Por que três clusters?\n\nEntre as alternativas de dois a seis grupos, três apresentou a melhor silhueta. O valor de 0,224 e o grupo de temperatura extrema mostram que ainda é preciso cuidado na interpretação.\n\n### O que poderia melhorar o classificador?\n\nAmpliar os dados e avaliar pesos das classes, parâmetros e limite de decisão no conjunto de desenvolvimento. São propostas que exigem novo teste, sem reutilizar o teste atual para escolher ajustes.\n\n### O modelo prevê uma falha antes de acontecer?\n\nA avaliação considera o rótulo no próprio registro. A previsão antecipada exigiria definir um horizonte futuro e utilizar somente informações anteriores a ele.\n\n### Por que usar Spark em uma base pequena?\n\nPara aplicar as operações de processamento solicitadas no projeto. O Pandas foi suficiente para este volume, e o trabalho não comprovou ganho de desempenho com Spark.\n';
await fs.writeFile(path.join(root,'entregas/Roteiro_Apresentacao.md'),md);
for(let i=0;i<p.slides.items.length;i++){
 const blob=await p.export({slide:p.slides.items[i],format:'png',scale:1});
 await fs.writeFile(path.join(build,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
}
const candidate=path.join(build,'rascunho.pptx');
await(await PresentationFile.exportPptx(p)).save(candidate);
const result=await finalizePresentation({workspaceDir:root,candidatePath:candidate,
 finalPath:path.join(root,'entregas/Apresentacao_Manutencao_Industrial.pptx'),
 pythonExecutable:'C:/Users/dsadm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',
 ...[3,5,7,8,9,11].flatMap(i=>['--require-native-table-slide',String(i)])],
 requiredNativeTableOwnerSlides:[3,5,7,8,9,11],requiredNativeChartOwnerSlides:[4,6],
 materializeLiteralChartWorkbooks:true,
 fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,
 receiptPath:path.join(build,'validacao.json')});
console.log(JSON.stringify(result));
